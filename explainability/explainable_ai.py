def generate_explanation(claim, fraud_result, severity):


    fraud_score = fraud_result.get(
        "fraud_score",
        0
    )


    severity_level = severity.get(
        "severity",
        "unknown"
    )



    if fraud_score > 70:

        reason = (
            "High fraud indicators detected. "
            "The claim requires detailed verification."
        )


        confidence = "85%"



    elif severity_level == "high":

        reason = (
            "Major damage detected from evidence images. "
            "Claim needs further inspection."
        )


        confidence = "80%"



    else:


        reason = (
            "Evidence and claim details appear consistent. "
            "No major suspicious activity detected."
        )


        confidence = "75%"




    return {


        "confidence": confidence,


        "reason": reason,


        "summary":
        "AI generated explanation based on fraud analysis and damage severity."

    }