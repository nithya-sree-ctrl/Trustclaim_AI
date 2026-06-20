def generate_explanation(claim, fraud_result, severity):


    fraud_score = fraud_result.get(
        "fraud_score",
        0
    )


    risk_level = fraud_result.get(
        "risk_level",
        "unknown"
    )


    flags = fraud_result.get(
        "flags",
        "none"
    )


    severity_level = severity.get(
        "severity",
        "unknown"
    )



    reasons = []



    # Fraud reasoning

    if fraud_score >= 70:

        reasons.append(
            "High fraud probability detected from claim patterns."
        )

    elif fraud_score >= 40:

        reasons.append(
            "Some suspicious indicators were found and require review."
        )

    else:

        reasons.append(
            "No major fraud indicators detected."
        )




    # Severity reasoning

    if severity_level == "high":

        reasons.append(
            "Image analysis indicates severe damage."
        )


    elif severity_level == "medium":

        reasons.append(
            "Image analysis indicates moderate damage."
        )


    elif severity_level == "low":

        reasons.append(
            "Only minor visible damage detected."
        )



    reason = " ".join(reasons)



    # Dynamic confidence

    confidence = max(
        100 - fraud_score,
        10
    )



    return {


        "confidence":
        f"{confidence}%",


        "reason":
        reason,


        "summary":

        f"""
        Claim: {claim}

        Severity assessment:
        {severity_level}

        Fraud risk:
        {risk_level}

        Risk indicators:
        {flags}
        """

    }