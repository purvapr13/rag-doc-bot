from fastapi import FastAPI, Body
import asyncio
import uvicorn
import logging

from app.utils.logger import configure_logging
from app.ingestion.vectorstore import ChromaVectorStore
from app.llm_engine import OllamaAnswerGenerator
from pydantic import BaseModel

configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI()

# Initialize vector store & Ollama generator
vector_store = ChromaVectorStore(
    persist_directory="chroma_db",
    local_model_path="app/models/all-MiniLM-L6-v2"
)

llm = OllamaAnswerGenerator(model_name="mistral")


class QuestionRequest(BaseModel):
    ques: str


@app.get("/")
def home():
    return {"message": "RAG chatbot is running. Use POST /predict with JSON body: {'ques': 'your question'}"}


@app.post("/predict")
async def predict(request: QuestionRequest = Body(...)):
    try:
        ques = request.ques
        logger.info(f"Received question: {ques}")

        top_docs = vector_store.similarity_search(ques, k=2)
        context = "\n\n".join([doc.page_content for doc in top_docs])

        logger.info("Generating answer using Ollama...")
        answer = llm.generate(context=context, question=ques)

        return {"question": ques, "answer": answer}

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"error": "Sorry, could not process your request."}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
