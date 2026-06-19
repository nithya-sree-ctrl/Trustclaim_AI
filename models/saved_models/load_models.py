from saved_models.model_config import (
    MODEL_CONFIG
)


def load_model(
    model_name
):

    return MODEL_CONFIG.get(
        model_name
    )