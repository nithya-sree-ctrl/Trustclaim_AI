from nlp.issue_classifier import classify_issue


class ClaimNLPModel:

    def analyze_claim(self, claim_text):

        issue_type = classify_issue(
            claim_text
        )

        return {
            "issue_type": issue_type,
            "claim_text": claim_text
        }