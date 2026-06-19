from fraud_detection.history_analyzer import get_user_risk


def evaluate_risk(
    user_id,
    duplicate_found,
    evidence_met
):

    risk_level = get_user_risk(user_id)

    risk_score = 0

    flags = []

    if risk_level == "high":
        risk_score += 40
        flags.append("frequent_claimant")

    elif risk_level == "medium":
        risk_score += 20

    if duplicate_found:
        risk_score += 30
        flags.append("duplicate_images")

    if not evidence_met:
        risk_score += 20
        flags.append("insufficient_evidence")

    risk_score = min(risk_score, 100)

    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "flags": flags if flags else ["none"]
    }