from pathlib import Path 


def create_metadata(file_name: str) -> dict:
    """ 
    Create metadata based on file name .
    """
    file_name_lower = file_name.lower()

    metadata = {

        "source": file_name,
        "policy_type":"unknown",
        "country":"global",
    }
    if "travel_policy_india" in file_name_lower:
        metadata["policy_type"] = "travel"
        metadata["country"] = "India"

    elif "travel_policy_us" in file_name_lower:
        metadata["policy_type"] = "travel"
        metadata["country"] = "US"

    # Other policies
    elif "airport_policy" in file_name_lower:
        metadata["policy_type"] = "airport"

    elif "employee_eligibility" in file_name_lower:
        metadata["policy_type"] = "employee_eligibility"

    elif "expense_policy" in file_name_lower:
        metadata["policy_type"] = "expense"

    elif "cancellation_policy" in file_name_lower:
        metadata["policy_type"] = "cancellation"

    elif "approval_policy" in file_name_lower:
        metadata["policy_type"] = "approval"

    return metadata


if __name__ == "__main__":

    files = [
        "travel_policy_india.txt",
        "travel_policy_us.txt",
        "airport_policy.txt",
        "employee_eligibility.txt",
        "expense_policy.txt",
        "cancellation_policy.txt",
        "approval_policy.txt"
    ]

    for file_name in files:
        print(file_name)
        print(create_metadata(file_name))
        print()