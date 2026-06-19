def generate_confidence(
    evidence_met,
    fraud_score,
    image_confidence
):

    score = image_confidence

    if evidence_met:
        score += 20

    score -= fraud_score * 0.20

    score = max(
        0,
        min(score, 100)
    )

    return round(score, 2)