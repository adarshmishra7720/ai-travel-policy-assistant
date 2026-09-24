import os
from pathlib import Path
import numpy as np
from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


client = genai.Client(api_key=api_key)


def create_embedding(text: str):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

    return np.dot(vector_a, vector_b) / (
        np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    )


def embed_chunks(chunk_records):
    """Create embeddings for all policy chunks."""

    embedded_chunks = []

    for chunk in chunk_records:

        embedding = create_embedding(
            chunk["text"]
        )

        embedded_chunk = chunk.copy()
        embedded_chunk["embedding"] = embedding

        embedded_chunks.append(
            embedded_chunk
        )

    return embedded_chunks


if __name__ == "__main__":

    from ingestion import load_documents
    from chunking import create_chunk_records

    documents = load_documents(
        Path(__file__).parent.parent / "data" / "company_policy"
    )

    all_chunks = []

    for document in documents:
        chunks = create_chunk_records(
            document,
            chunk_size=500
        )

        all_chunks.extend(chunks)

    print(f"Total chunks: {len(all_chunks)}")

    embedded_chunks = embed_chunks(all_chunks)

    print(
        f"Embedded chunks: {len(embedded_chunks)}"
    )

    print(
        f"Vector dimensions: "
        f"{len(embedded_chunks[0]['embedding'])}"
    )

    print(
        f"First chunk: "
        f"{embedded_chunks[0]['chunk_id']}"
    )