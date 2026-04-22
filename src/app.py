import streamlit as st
from retriever import create_vector_db
from rag_pipeline import get_answer
# Page config
st.set_page_config(page_title="College AI Assistant", layout="wide")

st.title("🎓 College Admission Assistant")
st.write("Ask anything about college admissions!")

# Load DB once (cache for performance)
@st.cache_resource
def load_db():
    return create_vector_db()

db = load_db()

# User input
query = st.text_input("Enter your question:")

if st.button("Ask"):
    if query:
        with st.spinner("Thinking..."):
            response = get_answer(query, db)
            st.success("Answer:")
            st.write(response)
    else:
        st.warning("Please enter a question.")