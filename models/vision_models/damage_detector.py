def detect_damage(
    gemini_response
):

    return {
        "damage_detected": True,
        "raw_response":
            gemini_response
    }