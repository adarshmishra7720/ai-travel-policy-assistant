from search import build_vector_store, search_policy
from gemini_client import ask_gemini



def answer_policy_question(store, question, top_k=3):

    results = search_policy(
        store,
        question,
        top_k=top_k
    )

    context_parts = []

    for result in results:

        chunk = result["chunk"]

        context_parts.append(
            f"Source: {chunk['document_name']}\n"
            f"Content:\n{chunk['text']}"
        )

    context = "\n\n---\n\n".join(
        context_parts
    )

    prompt = f"""
        You are a company travel policy assistant.

        Answer the user's question using ONLY the policy
        context provided below.

        Do not invent or assume policy rules.

        If the context does not contain enough information
        to answer the question, clearly say that the
        available policy information is insufficient.

        Policy Context:
        {context}

        User Question:
        {question}

        Answer clearly and concisely.
        """

    answer = ask_gemini(prompt)

    return answer, results



if __name__ == "__main__":

    store = build_vector_store()

    question = (
    "What is the maximum hotel reimbursement "
    "amount in India?"
     )

    answer, results = answer_policy_question(
        store,
        question
    )

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")

    for result in results:

        chunk = result["chunk"]

        print(
            f"- {chunk['document_name']} "
            f"({result['similarity']:.4f})"
        )