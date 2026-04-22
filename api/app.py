from fastapi import FastAPI
from src.retriever import create_vector_db
from src.rag_pipeline import get_answer

app = FastAPI()

# Load DB once
db = create_vector_db()


@app.get("/")
def home():
    return {"message": "College AI Assistant running 🚀"}


@app.get("/ask")
def ask(query: str):
    answer = get_answer(query, db)
    return {"response": answer}