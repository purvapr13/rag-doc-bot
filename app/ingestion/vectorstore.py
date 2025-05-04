import torch
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from app.utils.logger import configure_logging
import logging

configure_logging()
logger = logging.getLogger(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"


class ChromaVectorStore:
    def __init__(self, persist_directory="../chroma_db", local_model_path="../models/all-MiniLM-L6-v2"):
        self.persist_directory = persist_directory

        logger.info(f"Loading embeddings model on device: {device}")
        self.embedding_function = HuggingFaceEmbeddings(model_name=local_model_path,
                                                        model_kwargs={"device": device})

        logger.debug('Create or loading Chroma DB')
        self.db = Chroma(
            collection_name="document_chunks",
            embedding_function=self.embedding_function,
            persist_directory=self.persist_directory
        )

    def add_documents(self, documents: list[Document]):
        self.db.add_documents(documents)

    def similarity_search(self, query, k=5):
        return self.db.similarity_search(query, k=k)

    def as_retriever(self):
        return self.db.as_retriever()


