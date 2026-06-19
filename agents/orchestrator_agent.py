from agents.claim_agent import analyze_claim
from agents.image_agent import analyze_images

from agents.evidence_agent import (
    evaluate_evidence
)

from agents.fraud_agent import (
    calculate_fraud
)

from agents.severity_agent import (
    estimate_severity
)

from agents.adjuster_agent import (
    generate_recommendation
)


def process_claim(
    user_id,
    claim_text,
    claim_object,
    image_paths
):

    claim_data = analyze_claim(
        claim_text
    )

    image_data = analyze_images(
        image_paths
    )

    evidence = evaluate_evidence(
        claim_object,
        len(image_paths)
    )

    fraud = calculate_fraud(
        user_id,
        image_data["duplicate"],
        evidence["evidence_standard_met"]
    )

    severity = estimate_severity(
        image_data["damage"]
    )

    recommendation = (
        generate_recommendation(
            claim_data,
            image_data,
            fraud
        )
    )

    return {
        "claim": claim_data,
        "image": image_data,
        "evidence": evidence,
        "fraud": fraud,
        "severity": severity,
        "recommendation": recommendation
    }