from langchain_core.documents import Document
from src.ingestion import load_data
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FakeEmbeddings

def get_embeddings():
    return FakeEmbeddings(size=384)

def create_vector_db():
    raw_docs = load_data()

    docs = [
        Document(page_content=text, metadata=meta)
        for text, meta in raw_docs
    ]

    db = Chroma.from_documents(
        docs,
        get_embeddings(),
        persist_directory="chroma_db"
    )

    db.persist()
    print("✅ DB created")

    return db

def load_vector_db():
    return Chroma(
        persist_directory="chroma_db",
        embedding_function=get_embeddings()
    )