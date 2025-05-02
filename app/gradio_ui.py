import gradio as gr
import requests
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

API_URL = "http://localhost:8000/predict"


def chat_fn(message: str) -> str:
    try:
        logger.debug(f"Sending request to: {API_URL} with message: {message}")
        response = requests.post(API_URL, json={"ques": message}, timeout=10)
        response.raise_for_status()
        answer = response.json().get("answer", "No response from backend.")
        return answer
    except Exception as e:
        logger.error(f"Error in chat_fn: {e}")
        return f"❌ Error: {e}"


chat_ui = gr.ChatInterface(
    fn=chat_fn,
    title="🤖 RAG Doc Chatbot",
    theme="soft",
    examples=[
        "What is the company overview?",
        "List the risks mentioned.",
        "What are the financial highlights?"
    ]
)

if __name__ == "__main__":
    chat_ui.launch(inbrowser=True, debug=True)
