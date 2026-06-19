from agents.evidence_agent import (
    evaluate_evidence
)

from agents.severity_agent import (
    estimate_severity
)


def test_evidence_agent():

    result = evaluate_evidence(
        "car",
        3
    )

    assert (
        "evidence_standard_met"
        in result
    )


def test_severity_agent():

    severity = estimate_severity(
        "major crack on windshield"
    )

    assert severity in [
        "high",
        "medium",
        "low",
        "unknown"
    ]


if __name__ == "__main__":

    test_evidence_agent()

    test_severity_agent()

    print(
        "All agent tests passed."
    )