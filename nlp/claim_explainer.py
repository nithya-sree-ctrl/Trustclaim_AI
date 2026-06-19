def explain_claim(
    claim_status,
    issue_type,
    severity
):

    return (
        f"The claim was classified as "
        f"'{claim_status}' because "
        f"the detected issue is "
        f"'{issue_type}' with "
        f"'{severity}' severity."
    )