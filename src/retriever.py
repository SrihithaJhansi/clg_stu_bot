from langchain_core.documents import Document
from ingestion import load_data
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
def create_vector_db():
    raw_docs = load_data()

    docs = [
        Document(page_content=text, metadata=meta)
        for text, meta in raw_docs
    ]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(docs, embeddings)
    print(docs[0].page_content)
    return db