from fastapi import FastAPI
from pydantic import BaseModel
from agent import process_question

app = FastAPI()

class QuestionRequest(BaseModel):
    store_id: str
    question: str

@app.post("/ask")
def ask_question(req: QuestionRequest):
    return process_question(req.store_id, req.question)
