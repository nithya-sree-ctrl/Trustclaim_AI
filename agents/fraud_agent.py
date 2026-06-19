from fraud_detection.history_analyzer import get_user_risk


def calculate_fraud(
    user_id,
    duplicate_found,
    evidence_met
):

    score = 0

    risk_flags = []

    user_risk = get_user_risk(user_id)

    if user_risk == "high":
        score += 40
        risk_flags.append(
            "frequent_claimant"
        )

    elif user_risk == "medium":
        score += 20

    if duplicate_found:
        score += 30

        risk_flags.append(
            "duplicate_images_detected"
        )

    if not evidence_met:
        score += 20

        risk_flags.append(
            "insufficient_evidence"
        )

    score = min(score, 100)

    if not risk_flags:
        risk_flags.append("none")

    return {
        "fraud_score": score,
        "risk_flags": risk_flags
    }