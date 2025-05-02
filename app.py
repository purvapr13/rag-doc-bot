from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_ques():
    return {"Please wait..."}


@app.get("/predict")
def response_gen(ques: str):
    try:
        print("write a function")
    except Exception as e:
        return {"sorry, couldn't process the request."}

