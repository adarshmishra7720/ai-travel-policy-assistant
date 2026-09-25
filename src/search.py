from pathlib import Path

from ingestion import load_documents
from chunking import create_chunk_records
from embeddings import create_embedding
from vector_store import VectorStore




PROJECT_ROOT = Path(__file__).parent.parent
POLICY_DIR = PROJECT_ROOT / "data" / "company_policy"


def build_vector_store():

    documents = load_documents(POLICY_DIR)

    store = VectorStore()

    for document in documents:

        chunks = create_chunk_records(
            document,
            chunk_size=500
        )

        for chunk in chunks:

            embedding = create_embedding(
                chunk["text"]
            )

            chunk["embedding"] = embedding

            store.add(chunk)

    return store


def search_policy(store, query, top_k=3):

    query_embedding = create_embedding(query)

    results = store.search(
        query_embedding,
        top_k=top_k
    )

    return results



if __name__ == "__main__":

    store = build_vector_store()

    query = (
        "Are personal airport trips reimbursable?"
    )

    results = search_policy(
        store,
        query,
        top_k=3
    )

    print("\nQuery:")
    print(query)

    print("\nRetrieved policies:")

    for result in results:

        chunk = result["chunk"]

        print("\n------------------------------")
        print(
            f"Similarity: "
            f"{result['similarity']:.4f}"
        )
        print(
            f"Source: "
            f"{chunk['document_name']}"
        )
        print(
            f"Chunk ID: "
            f"{chunk['chunk_id']}"
        )
        print("Text:")
        print(chunk["text"])