from fraud_detection.detector import detect_fraud
from severity.analyzer import calculate_severity
from explainability.explainable_ai import generate_explanation
from image_analysis.opencv_analyzer import analyze_damage



def process_claim(claim, image_paths=None):


    # Fraud analysis
    fraud_result = detect_fraud(claim)



    # OpenCV image analysis
    image_result = analyze_damage(
        image_paths
    )



    # Severity analysis
    severity_result = calculate_severity(
        image_result
    )



    # Explanation needs claim + fraud + severity
    explanation = generate_explanation(
        claim,
        fraud_result,
        severity_result
    )



    result = {


        "claim": claim,


        "image": image_result,


        "fraud": fraud_result,


        "severity": severity_result,


        "explanation": explanation,


        "status":
        "Analyzed successfully"


    }


    return result