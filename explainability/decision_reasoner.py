def generate_reasoning(
    claim_status,
    severity,
    fraud_score
):

    return (
        f"Claim status is '{claim_status}'. "
        f"Detected severity is '{severity}'. "
        f"Fraud score is {fraud_score}. "
        f"Decision generated from visual evidence and risk analysis."
    )