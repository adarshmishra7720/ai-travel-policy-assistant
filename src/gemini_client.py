import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


client = genai.Client(api_key=api_key)


def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    

    context = """
    Standard airport trip limits:
    - India: INR 2,000
    - United States: USD 75

    Late-night airport trips are allowed between 10:00 PM and 6:00 AM.
    """

    question = "What is the standard airport reimbursement limit in India?"

    prompt = f"""
    You are a corporate travel policy assistant.

    Answer the user's question using ONLY the provided policy context.

    Do not invent policy rules or reimbursement limits.

    Policy Context:
    {context}

    User Question:
    {question}

    Answer:
    """

    answer = ask_gemini(prompt)

    print(answer)