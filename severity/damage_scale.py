DAMAGE_SCALE = {

    "none": 0,

    "low": 25,

    "medium": 50,

    "high": 100
}


def get_damage_score(
    severity
):

    return DAMAGE_SCALE.get(
        severity.lower(),
        0
    )