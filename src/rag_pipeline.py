import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-lite")


def get_answer(query, db):
    docs = db.similarity_search(query, k=3)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are a college admission assistant.

Use ONLY the provided context.
If information is missing, say "I don't know".

Context:
{context}

Question:
{query}

Answer in clear bullet points.
"""

    response = model.generate_content(prompt)
    print("CONTEXT SENT TO LLM:\n", context)
    return response.text