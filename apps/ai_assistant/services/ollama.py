import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi4-mini:latest"


def generate_answer(*, question: str, context: str) -> str:
    prompt = f"""
You are a meeting intelligence assistant.

Answer the question using the provided meeting notes.

Rules:
1. Use information from the context.
2. If the context directly mentions the topic, summarize what it says.
3. Do not say information is missing if the context clearly contains relevant information.
4. Do not invent facts that are not present.
5. Keep the answer concise.

Context:
{context}

Question:
{question}

Answer:
"""



    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
        },
        timeout=120,
    )

    response.raise_for_status()

    data = response.json()

    return data["response"].strip()