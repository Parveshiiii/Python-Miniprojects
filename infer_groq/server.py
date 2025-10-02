from fastapi import FastAPI
from pydantic import BaseModel
from client import chat
app = FastAPI()

class Input(BaseModel):
    content: str

@app.post("/generate")
def output(input:Input):
    message = chat(input.content)
    return {"response": message}

