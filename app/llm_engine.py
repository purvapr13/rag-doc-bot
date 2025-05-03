import requests
import logging

from app.utils.logger import configure_logging
configure_logging()
logger = logging.getLogger(__name__)


class OllamaAnswerGenerator:
    def __init__(self, model_name="mistral", base_url="http://localhost:11434"):
        logger.info('initialising ollama model server')
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
            "stream": False
        }

        response = requests.post(f"{self.base_url}/api/generate", json=payload)
        logger.info(f"generated ollama model response: {response.text}")
        response.raise_for_status()
        return response.json()["response"].strip()
