from embeddings import cosine_similarity


class VectorStore:

    def __init__(self):
        self.chunks = []

    def add(self, chunk):
        self.chunks.append(chunk)

    def search(self, query_embedding, top_k=3):

        results = []

        for chunk in self.chunks:

            similarity = cosine_similarity(
                query_embedding,
                chunk["embedding"]
            )

            results.append({
                "chunk": chunk,
                "similarity": similarity
            })

        results.sort(
            key=lambda result: result["similarity"],
            reverse=True
        )

        return results[:top_k]


if __name__ == "__main__":

    store = VectorStore()

    store.add({
        "chunk_id": "chunk_1",
        "text": "India airport reimbursement limit.",
        "embedding": [1, 0, 0]
    })

    store.add({
        "chunk_id": "chunk_2",
        "text": "Cancellation policy.",
        "embedding": [0, 1, 0]
    })

    store.add({
        "chunk_id": "chunk_3",
        "text": "US travel policy.",
        "embedding": [0, 0, 1]
    })

    query_embedding = [0.9, 0.1, 0]

    results = store.search(
        query_embedding,
        top_k=2
    )

    for result in results:
        print(
            result["chunk"]["chunk_id"],
            result["similarity"]
        )