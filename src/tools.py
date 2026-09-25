EMPLOYEES = {
    "EMP001": {
        "country": "India",
        "employee_type": "Full-Time",
        "status": "Eligible",
        "manager_approval": "Yes"
    },
    "EMP002": {
        "country": "India",
        "employee_type": "Contractor",
        "status": "Approval Required",
        "manager_approval": "No"
    },
    "EMP003": {
        "country": "United States",
        "employee_type": "Full-Time",
        "status": "Eligible",
        "manager_approval": "Yes"
    },
    "EMP004": {
        "country": "United States",
        "employee_type": "Contractor",
        "status": "Not Eligible",
        "manager_approval": "No"
    },
    "EMP005": {
        "country": "India",
        "employee_type": "Full-Time",
        "status": "Eligible",
        "manager_approval": "Yes"
    },
    "EMP006": {
        "country": "United States",
        "employee_type": "Full-Time",
        "status": "Approval Required",
        "manager_approval": "No"
    }
}


def check_employee_eligibility(employee_id):
    employee = EMPLOYEES.get(employee_id)

    if employee is None:
        return {
            "employee_id": employee_id,
            "status": "Unknown",
            "reason": "Employee ID was not found."
        }

    return {
        "employee_id": employee_id,
        "status": employee["status"],
        "country": employee["country"],
        "employee_type": employee["employee_type"],
        "manager_approval": employee["manager_approval"]
    }


def is_late_night(time):
    hour = int(time.split(":")[0])

    return hour >= 22 or hour < 6


def validate_trip(employee_id, trip_type, amount, time):
    employee = EMPLOYEES.get(employee_id)

    # Employee not found
    if employee is None:
        return {
            "employee_id": employee_id,
            "status": "Invalid",
            "reason": "Employee ID was not found."
        }

    # Employee not eligible
    if employee["status"] == "Not Eligible":
        return {
            "employee_id": employee_id,
            "status": "Not Eligible",
            "reason": "Employee is not eligible for reimbursement."
        }

    late_night = is_late_night(time)

    # India airport policy
    if (
        employee["country"] == "India"
        and trip_type.lower() == "airport"
    ):
        policy_limit = 2000

        # Amount within limit
        if amount <= policy_limit:

            if late_night:
                return {
                    "employee_id": employee_id,
                    "status": "Approved",
                    "reason": (
                        "Late-night business travel is allowed and "
                        "the trip amount is within the standard limit."
                    )
                }

            return {
                "employee_id": employee_id,
                "status": "Approved",
                "reason": (
                    "Trip amount is within the standard "
                    "airport reimbursement limit."
                )
            }

        # Amount above limit + late night
        if late_night:
            return {
                "employee_id": employee_id,
                "status": "Needs Approval",
                "reason": (
                    "Late-night business travel is allowed, but the "
                    "trip amount exceeds the standard INR 2,000 limit "
                    "and requires approval."
                )
            }

        # Amount above limit
        return {
            "employee_id": employee_id,
            "status": "Needs Approval",
            "reason": (
                "Trip amount exceeds the standard limit of INR 2,000. "
                "Additional approval is required."
            )
        }

    # No matching rule
    return {
        "employee_id": employee_id,
        "status": "Needs Review",
        "reason": (
            "No specific validation rule was found for this trip."
        )
    }


if __name__ == "__main__":

    test_cases = [
        ("EMP001", "airport", 1500, "21:00"),
        ("EMP001", "airport", 2500, "22:30"),
        ("EMP004", "airport", 1500, "21:00"),
        ("EMP999", "airport", 1500, "21:00"),
    ]

    for employee_id, trip_type, amount, time in test_cases:
        result = validate_trip(
            employee_id,
            trip_type,
            amount,
            time
        )

        print(result)