from severity.severity_predictor import estimate_severity


def calculate_severity(image_paths):

    image_analysis = "vehicle damaged with crack"

    severity = estimate_severity(
        image_analysis
    )

    return {
        "severity": severity,
        "status": "Severity analysis completed"
    }