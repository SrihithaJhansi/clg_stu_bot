from typing import Any
from src.rag_pipeline import get_answer
from src.retriever import create_vector_db


class SimpleOrchestration:
    def __init__(self):
        self.db = create_vector_db()

    def process_query(self, query: str) -> str:
        return get_answer(query, self.db)


def create_orchestrator(mode: str = "simple") -> Any:
    return SimpleOrchestration()