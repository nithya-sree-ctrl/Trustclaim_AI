from fraud_detection.risk_flag_generator import generate_risk_flags
from fraud_detection.history_analyzer import get_user_risk


def calculate_score(num_images, duplicate_found):

    score = 10

    if num_images < 2:
        score += 30

    if duplicate_found:
        score += 40

    return min(score, 100)



def detect_fraud(claim):

    # temporary values
    num_images = 1
    duplicate_found = False


    score = calculate_score(
        num_images,
        duplicate_found
    )


    risk = get_user_risk(
        1
    )


    flags = generate_risk_flags(
        duplicate_found,
        True,
        score
    )


    return {

        "fraud_score": score,

        "risk_level": risk,

        "flags": flags,

        "status": "Fraud analysis completed"

    }