def generate_reason(claim, fraud_result):


    score = fraud_result.get(
        "fraud_score",
        0
    )


    if score < 40:

        return "Claim appears genuine based on low fraud indicators"


    elif score < 70:

        return "Claim requires manual review"


    else:

        return "High fraud possibility detected"