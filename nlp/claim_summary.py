import google.generativeai as genai
from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_claim(text):

    prompt = f"""
    Summarize this insurance claim.

    Claim:
    {text}

    Give:
    - Issue Type
    - Damaged Part
    - Short Summary
    """

    response = model.generate_content(prompt)

    return response.text