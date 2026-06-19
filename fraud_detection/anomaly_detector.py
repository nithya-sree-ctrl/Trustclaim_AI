def detect_anomalies(
    fraud_score,
    duplicate_found,
    claim_count
):

    anomalies = []

    if duplicate_found:
        anomalies.append(
            "Duplicate image detected"
        )

    if claim_count > 10:
        anomalies.append(
            "Frequent claimant"
        )

    if fraud_score > 70:
        anomalies.append(
            "High fraud score"
        )

    return anomalies