from PIL import Image
import google.generativeai as genai
from backend.config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def analyze_damage(image_path):

    image = Image.open(image_path)

    prompt = """
    Analyze this insurance image.

    Return JSON:

    {
      "object_type":"",
      "damaged_part":"",
      "issue_type":"",
      "severity":"",
      "confidence":""
    }
    """

    response = model.generate_content(
        [prompt, image]
    )

    return response.text