from nlp.issue_classifier import (
    classify_issue
)


def test_claim_classification():

    issue = classify_issue(
        "There is a crack on my laptop screen."
    )

    assert issue == "crack"


def test_unknown_claim():

    issue = classify_issue(
        "Everything looks normal."
    )

    assert issue == "unknown"


if __name__ == "__main__":

    test_claim_classification()

    test_unknown_claim()

    print(
        "Claim tests passed."
    )