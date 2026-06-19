def generate_recommendation(
    claim_data,
    image_data,
    fraud_data
):

    score = fraud_data["fraud_score"]

    if score < 30:
        return "Approve Claim"

    if score < 60:
        return "Manual Review Required"

    return "Potential Fraud Investigation"