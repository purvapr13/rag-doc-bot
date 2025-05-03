import logging
import os
import requests
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from app.utils.logger import configure_logging

configure_logging()
logger = logging.getLogger(__name__)


# Custom Answer Generator using Ollama
class OllamaAnswerGenerator:
    def __init__(self, model_name="mistral", base_url="http://localhost:11434"):
        logger.info("Initialising Ollama model server")
        self.model_name = model_name
        self.base_url = base_url

    def generate(self, context: str, question: str) -> str:
        prompt = f"""You are a helpful assistant. Answer the question only using the context below.

Context:
{context}

Answer the following question strictly based on the context. Do not invent any information.

Question: {question}
Answer:"""

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
        }

        response = requests.post(f"{self.base_url}/api/generate", json=payload)
        logger.info(f"Generated Ollama model response: {response.text}")
        response.raise_for_status()
        return response.json()["response"].strip()


# Resolve model path relative to project root
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(current_dir)
model_path = os.path.join(current_dir, "app", "models", "all-MiniLM-L6-v2")
chroma_db_path = os.path.join(current_dir, "app", "chroma_db")


# Custom wrapper for vector store
class ChromaVectorStore:
    def __init__(self, persist_directory=chroma_db_path, local_model_path=model_path,
                 collection_name="document_chunks"):
        logger.debug("Initializing embedding model")
        self.embedding_function = HuggingFaceEmbeddings(model_name=local_model_path)

        logger.debug("Creating or loading Chroma DB")
        self.db = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embedding_function,
            collection_name="document_chunks"
        )

    def similarity_search(self, query, k=5):
        return self.db.similarity_search(query, k=k)

    def as_retriever(self, **kwargs):
        return self.db.as_retriever(**kwargs)


# Retrieval QA System using LangChain + Ollama
class LangChainRetrievalQA:
    def __init__(self, vector_store: ChromaVectorStore, model_name="mistral", base_url="http://localhost:11434"):
        self.vector_store = vector_store
        self.ollama_answer_generator = OllamaAnswerGenerator(model_name=model_name, base_url=base_url)

    def _create_retriever(self):
        return self.vector_store.as_retriever()

    def _generate_answer(self, context: str, question: str) -> str:
        return self.ollama_answer_generator.generate(context=context, question=question)

    def get_answer(self, question: str) -> str:
        retriever = self._create_retriever()
        documents = retriever.invoke(question)

        if not documents:
            logger.warning("No relevant documents found for the question.")
            return "⚠️ Sorry, I couldn't find relevant information in the documents."

        context = "\n\n".join([doc.page_content for doc in documents])
        return self._generate_answer(context=context, question=question)


# Initialize Chroma vector store
vector_store = ChromaVectorStore(persist_directory=chroma_db_path, local_model_path=model_path,
                                 collection_name="document_chunks")
print("Document count in DB:", vector_store.db._collection.count())


# Initialize LangChain Retrieval QA instance
qa_system = LangChainRetrievalQA(vector_store)

# Example usage to get answer
# if __name__ == "__main__":
#     question = "What are the financial highlights for the year 2023?"
#     answer = qa_system.get_answer(question)
#     print(f"Answer: {answer}")
