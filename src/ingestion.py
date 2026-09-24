from pathlib import Path
from preprocessing import clean_text
from metadata import create_metadata
from chunking import create_chunk_records


# POLICY_DIR = Path("data/company_policy")
PROJECT_ROOT = Path(__file__).parent.parent
POLICY_DIR = PROJECT_ROOT / "data" / "company_policy"


def load_documents(policy_dir: Path):
    documents = []

    if not policy_dir.exists():
        raise FileNotFoundError(
            f"Policy directory not found: {policy_dir}"
        )

    for file_path in policy_dir.glob("*.txt"):

        raw_content = file_path.read_text(
            encoding="utf-8"
        ).strip()

        content = clean_text(raw_content)

        if not content:
            print(f"WARNING: Empty document: {file_path.name}")
            continue

        # documents.append({
        #     "document_name": file_path.name,
        #     "content": content
        # })

        metadata = create_metadata(file_path.name)
        documents.append({
            "document_name": file_path.name,
            "content": content,
            "metadata": metadata
        })

    if not documents:
        print("WARNING: No valid policy documents found.")

    return documents


if __name__ == "__main__":

    documents = load_documents(POLICY_DIR)

    print(f"Loaded documents: {len(documents)}")

    for document in documents:

     chunk_records = create_chunk_records(document, chunk_size=500)
     print(f"\n{document['document_name']}")
     print(f"Number of chunks: {len(chunk_records)}")
     for chunk in chunk_records:
        print(f"\n--- {chunk['chunk_id']} ---")
        print(chunk["text"])
        print(f"Metadata: {chunk['metadata']}")