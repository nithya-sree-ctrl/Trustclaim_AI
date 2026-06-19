def detect_object(
    gemini_response
):

    response = gemini_response.lower()

    if "car" in response:
        return "car"

    if "laptop" in response:
        return "laptop"

    if "package" in response:
        return "package"

    return "unknown"