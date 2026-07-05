import os
from dotenv import load_dotenv
from google import genai #to import the load_dotenv function from the dotenv module,


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_answer(question: str, retrieved_chunks: list) -> str:
    context = "\n\n".join(
        [chunk["content"] for chunk in retrieved_chunks]
    )

    prompt = f"""
You are a Knowledge Base Assistant.

Answer the user's question using ONLY the context below.

If the answer is not found in the context, say:
"The information is not available in the Knowledge Base."

Do not use outside knowledge.
Do not guess.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content( #to generate a response from the Gemini model using the provided prompt. The model is specified as "gemini-2.5-flash", and the contents of the prompt are passed to the model for processing.
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text