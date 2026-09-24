import re


def split_into_paragraphs(text: str):
    """Split text using blank lines as natural boundaries."""

    paragraphs = re.split(r"\n\s*\n", text)

    return [
        paragraph.strip()
        for paragraph in paragraphs
        if paragraph.strip()
    ]


def chunk_text(text: str, chunk_size: int = 500):
    """Create chunks using paragraph boundaries."""

    if not text:
        return []

    paragraphs = split_into_paragraphs(text)

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:

        if len(current_chunk) + len(paragraph) <= chunk_size:

            if current_chunk:
                current_chunk += "\n\n"

            current_chunk += paragraph

        else:

            if current_chunk:
                chunks.append(current_chunk.strip())

            current_chunk = paragraph

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def create_chunk_records(document: dict, chunk_size: int = 500):
    """Create chunks while preserving document metadata."""

    chunks = chunk_text(
        document["content"],
        chunk_size=chunk_size
    )

    chunk_records = []

    for index, chunk in enumerate(chunks, start=1):
        chunk_records.append({
            "chunk_id": f"{document['document_name']}_{index}",
            "text": chunk,
            "document_name": document["document_name"],
            "metadata": document["metadata"]
        })

    return chunk_records

if __name__ == "__main__":

    sample_text = """
    India Travel Policy

    Employees may use company-sponsored rides for approved business travel.

    The standard reimbursement limit for an individual business ride
    is INR 2,000 per trip.

    Trips above this limit require additional approval.

    Business travel between 10:00 PM and 6:00 AM is permitted
    when related to approved business activity.
    """

    chunks = chunk_text(
        sample_text
       
        
    )

    print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks, start=1):

        print(f"\n--- Chunk {i} ---")
        print(chunk)