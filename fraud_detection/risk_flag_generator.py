def generate_risk_flags(
    duplicate_found,
    evidence_met,
    fraud_score
):

    flags = []

    if duplicate_found:
        flags.append(
            "duplicate_images"
        )

    if not evidence_met:
        flags.append(
            "insufficient_evidence"
        )

    if fraud_score > 70:
        flags.append(
            "high_fraud_risk"
        )

    if not flags:
        flags.append("none")

    return ";".join(flags)