import os
from langchain_community.document_loaders import PyMuPDFLoader, Docx2txtLoader
from langchain_community.document_loaders import UnstructuredPowerPointLoader
from langchain_community.document_loaders.image import UnstructuredImageLoader
from app.utils.logger import configure_logging
import logging


configure_logging()
logger = logging.getLogger(__name__)


def extract_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    logger.info('loading pdf file')
    data = loader.load()
    return data


def extract_worddoc(file_path):
    loader = Docx2txtLoader(file_path)
    logger.info('loading word file')
    data = loader.load()
    return data


def extract_ppt(file_path):
    loader = UnstructuredPowerPointLoader(file_path)
    logger.info('loading ppt file')
    data = loader.load()
    return data


def extract_txt_frm_img(file_path):
    loader = UnstructuredImageLoader(file_path)
    logger.info('loading image file')
    data = loader.load()
    return data


def extract_text(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: {file_path}")

    ext = os.path.splitext(file_path)[-1].lower()

    if ext == '.pdf':
        return extract_pdf(file_path)
    elif ext == '.docx':
        return extract_worddoc(file_path)
    elif ext == '.pptx':
        return extract_ppt(file_path)
    elif ext == '.png':
        return extract_txt_frm_img(file_path)
    else:
        logger.error('given file format not supported')
        raise ValueError(f"Unsupported file format: {ext}")


