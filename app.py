from fastapi import FastAPI
import uvicorn

from app.utils.logger import configure_logging
import logging

configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def read_ques():
    logger.info('Getting question from the user:')
    return {"Please wait..."}


@app.get("/predict")
def response_gen(ques: str):
    try:
        logger.info('Generating answer:')
        print("write a function")
    except Exception as e:
        return {"sorry, couldn't process the request."}


# Main function to run the app
if __name__ == "__main__":
    uvicorn.run(app, port=8000)


