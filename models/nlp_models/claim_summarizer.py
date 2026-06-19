def summarize_claim(
    claim_text
):

    words = claim_text.split()

    return " ".join(
        words[:20]
    )