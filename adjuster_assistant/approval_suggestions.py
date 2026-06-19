def get_approval_suggestion(
    fraud_score,
    severity,
    evidence_met
):

    if not evidence_met:
        return {
            "status": "Pending",
            "suggestion": "Request Additional Evidence"
        }

    if fraud_score >= 70:
        return {
            "status": "Investigate",
            "suggestion": "Potential Fraud Detected"
        }

    if severity == "high":
        return {
            "status": "Approve",
            "suggestion": "Fast Track High Damage Claim"
        }

    if severity in ["medium", "low"]:
        return {
            "status": "Approve",
            "suggestion": "Standard Approval Process"
        }

    return {
        "status": "Manual Review",
        "suggestion": "Adjuster Verification Needed"
    }