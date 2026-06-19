def generate_adjuster_report(
    claim_summary,
    fraud_score,
    severity,
    evidence_met
):

    if fraud_score > 70:

        recommendation = (
            "Investigate Claim"
        )

    elif severity == "high":

        recommendation = (
            "Approve High Priority"
        )

    elif not evidence_met:

        recommendation = (
            "Request More Evidence"
        )

    else:

        recommendation = (
            "Approve Claim"
        )

    return {
        "recommendation":
            recommendation,

        "fraud_score":
            fraud_score,

        "severity":
            severity,

        "evidence_met":
            evidence_met,

        "adjuster_notes":
            (
                f"Severity: {severity}. "
                f"Fraud Score: {fraud_score}."
            )
    }