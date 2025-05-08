from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.utils.logger import configure_logging
import logging

configure_logging()
logger = logging.getLogger(__name__)


def preprocess_and_chunk(documents, chunk_size=900, chunk_overlap=100):
    logger.debug('Extract raw text from Document objects')
    all_text = [doc.page_content for doc in documents if doc.page_content.strip()]

    logger.debug('Initialize text splitter')
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    logger.debug('Create chunks')
    chunks = splitter.create_documents(all_text)

    return chunks  # List[Document] with metadata preserved
