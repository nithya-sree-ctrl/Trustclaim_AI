import google.generativeai as genai
from PIL import Image

from backend.config import (
    GEMINI_API_KEY
)

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def analyze_image(
    image_path
):

    image = Image.open(
        image_path
    )

    prompt = """
    Analyze this insurance image.

    Detect:

    1. Object Type
    2. Damaged Part
    3. Issue Type
    4. Severity

    Return JSON.
    """

    response = model.generate_content(
        [prompt, image]
    )

    return response.text