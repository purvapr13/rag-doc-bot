from app.ingestion.extractor import extract_text
from app.ingestion.chunker import preprocess_and_chunk
from app.ingestion.vectorstore import ChromaVectorStore
import logging
import os


model_path = os.path.abspath("../../app/models/all-MiniLM-L6-v2")

# Initialize Chroma VectorStore
vector_store = ChromaVectorStore(persist_directory="../chroma_db", local_model_path=model_path)

# Logger setup
logger = logging.getLogger(__name__)


def process_and_store_document(file_path):
    """
    Extract text, chunk it, generate embeddings, and store in Chroma DB.
    Args:
    - file_path: The path to the document (PDF, DOCX, PPTX, PNG, etc.)
    """
    try:
        # Extract text from the document (could be PDF, DOCX, PPTX, etc.)
        logger.info(f"Extracting text from {file_path}")
        documents = extract_text(file_path)

        # Preprocess and chunk the extracted text
        logger.info("Preprocessing and chunking extracted text")
        chunks = preprocess_and_chunk(documents)

        # Store the chunks in the Chroma vector store (embedding and saving)
        logger.info(f"Storing {len(chunks)} chunks into Chroma DB")
        vector_store.add_documents(chunks)

        logger.info(f"Successfully processed and stored document: {file_path}")
        print("Document count in DB:",
              vector_store.db._collection.count())  # or vector_store.db._collection.count_documents()


    except Exception as e:
        logger.error(f"Error processing {file_path}: {str(e)}")
        raise e


if __name__ == "__main__":
    file_path = "../data/goog-10-k-2023.pdf"
    process_and_store_document(file_path)
