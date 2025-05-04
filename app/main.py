from fastapi import FastAPI, Body
import uvicorn
import logging
from pydantic import BaseModel
import os

# Import custom logger and other components
from app.utils.logger import configure_logging
from app.retrieval import LangChainRetrievalQA, ChromaVectorStore

configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI()

# Resolve paths for the Chroma DB and models from the app directory
current_dir = os.path.dirname((os.path.abspath(__file__)))
model_path = os.path.join(current_dir, "models", "all-MiniLM-L6-v2")
chroma_db_path = os.path.join(current_dir, "chroma_db")

# Initialize the vector store and QA system
vector_store = ChromaVectorStore(persist_directory=chroma_db_path, local_model_path=model_path)
qa_system = LangChainRetrievalQA(vector_store)


# Define the request model
class QuestionRequest(BaseModel):
    ques: str


# Define the FastAPI POST endpoint
@app.post("/predict")
async def predict(request: QuestionRequest = Body(...)):
    try:
        question = request.ques
        logger.info(f"Received question: {question}")
        answer = qa_system.get_answer(question)
        return {"question": question, "answer": answer}
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"error": "Unable to process your request."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
