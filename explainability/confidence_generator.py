def generate_confidence(fraud_result):

    score = fraud_result.get(
        "fraud_score",
        0
    )


    confidence = 100 - score


    return str(confidence) + "%"