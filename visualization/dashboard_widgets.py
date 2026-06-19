def fraud_gauge(score):

    if score <= 30:
        return {
            "label": "Low Risk",
            "value": score
        }

    elif score <= 70:
        return {
            "label": "Medium Risk",
            "value": score
        }

    return {
        "label": "High Risk",
        "value": score
    }