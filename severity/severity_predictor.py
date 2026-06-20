def predict_severity(image_analysis):

    analysis_text = str(image_analysis).lower()


    if any(
        word in analysis_text
        for word in [
            "total damage",
            "shattered",
            "broken",
            "major crack",
            "severe"
        ]
    ):
        return "high"


    if any(
        word in analysis_text
        for word in [
            "dent",
            "medium",
            "crack",
            "damaged"
        ]
    ):
        return "medium"


    if any(
        word in analysis_text
        for word in [
            "scratch",
            "minor",
            "small mark"
        ]
    ):
        return "low"


    return "unknown"



# Used by analyzer.py
def estimate_severity(image_analysis):

    severity = predict_severity(
        image_analysis
    )

    return severity