from fraud_detection.detector import detect_fraud
from severity.analyzer import calculate_severity
from explainability.explainer import generate_explanation


def process_claim(claim, image_paths=None):


    fraud_result = detect_fraud(claim)

    severity_result = calculate_severity(image_paths)


    explanation = generate_explanation(
        claim,
        fraud_result
    )


    result = {


        "claim": claim,


        "image":{
            "damage":"Damage analysis completed",
            "uploaded_images":image_paths
        },


        "fraud":fraud_result,


        "severity":severity_result,


        "explanation":explanation,


        "status":"Analyzed successfully"


    }


    return result