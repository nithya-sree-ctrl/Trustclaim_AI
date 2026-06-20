from explainability.confidence_generator import generate_confidence
from explainability.decision_reasoner import generate_reason


def generate_explanation(claim, fraud_result):

    confidence = generate_confidence(
        fraud_result
    )

    reason = generate_reason(
        claim,
        fraud_result
    )

    return {

        "claim": claim,

        "confidence": confidence,

        "reason": reason,

        "summary": "AI generated explanation completed"

    }