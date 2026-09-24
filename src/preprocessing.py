import re


def clean_text(text: str) -> str:
    """
    Clean and normalize policy document text.
    """

    if not text:
        return ""

    # Remove whitespace at the beginning and end
    text = text.strip()

    # Normalize Windows line endings
    text = text.replace("\r\n", "\n")

    # Convert tabs to spaces
    text = text.replace("\t", " ")

    # Replace multiple spaces with one space
    text = re.sub(r"[ ]{2,}", " ", text)

    # Replace 3+ consecutive blank lines with 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text



if __name__ == "__main__":

    sample_text = """
    
    
    India Travel Policy
    
    
    Standard Business Travel Limit:     INR 2,000
    
    
    Airport Trips are allowed.
    
    
    """

    cleaned_text = clean_text(sample_text)

    print("BEFORE:")
    print(sample_text)

    print("\nAFTER:")
    print(cleaned_text)