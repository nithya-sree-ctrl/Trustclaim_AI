def generate_claim_summary(
    claim_text,
    issue_type,
    severity
):

    return {
        "summary":
            f"Claim reports "
            f"{issue_type} damage. "
            f"Estimated severity: "
            f"{severity}.",

        "original_claim":
            claim_text
    }