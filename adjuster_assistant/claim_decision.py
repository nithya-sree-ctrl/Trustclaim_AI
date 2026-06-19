def generate_claim_decision(
    evidence_met,
    fraud_score,
    damage_detected
):

    if not evidence_met:
        return "not_enough_information"

    if fraud_score > 80:
        return "contradicted"

    if damage_detected:
        return "supported"

    return "not_enough_information"