import pandas as pd

def classify_log(message):

    if pd.isna(message):
        return ("Unknown", "Low", "")

    text = str(message).lower()

    # Database
    if "foreign key" in text or "sql" in text:
        return (
            "Database",
            "Critical",
            "Verify SQL objects, constraints and database connectivity."
        )

    # Network
    if "network" in text:
        return (
            "Network",
            "High",
            "Check network connectivity and firewall."
        )

    # Web Service
    if "http" in text and "unavailable" in text:
        return (
            "Service",
            "High",
            "Verify the dependent web service endpoint."
        )

    # Memory
    if "out of memory" in text:
        return (
            "Memory",
            "Critical",
            "Increase memory or optimize batch processing."
        )

    return (
        "Application",
        "Medium",
        "Review application logs."
    )


def refine_message(message):

    if pd.isna(message):
        return ""

    text = str(message)

    if "dv_registration_itrg" in text:
        return "Driver registration failed because the user could not be assigned to a DV profile."

    if "Could not open a connection to SQL Server" in text:
        return "Application could not connect to SQL Server."

    if "unexpected network error" in text.lower():
        return "Unexpected network connectivity failure occurred."

    if "http" in text.lower() and "unavailable" in text.lower():
        return "Dependent web service is unavailable. The endpoint is unreachable or not responding."

    return text