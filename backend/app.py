from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.orchestration import create_orchestrator
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ORCHESTRATION_MODE = os.getenv("ORCHESTRATION_MODE", "simple")
orchestrator = create_orchestrator(mode=ORCHESTRATION_MODE)

@app.get("/health")
def health():
    return {"status": "healthy", "mode": ORCHESTRATION_MODE}

@app.get("/ask")
def ask(query: str, mode: str = ORCHESTRATION_MODE):
    try:
        answer = orchestrator.process_query(query)
        return {"query": query, "response": answer}
    except Exception as e:
        return {"error": str(e)}