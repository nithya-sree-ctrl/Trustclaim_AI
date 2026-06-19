from nlp.claim_summary import summarize_claim

def analyze_claim(claim_text):

    summary = summarize_claim(claim_text)

    return {
        "summary": summary
    }