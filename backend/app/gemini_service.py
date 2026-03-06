import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_explanation(text, emotions, risk_level):

    prompt = f"""
            You are an AI system that analyzes emotional manipulation in media.

            Text:
            {text}

            Detected emotions:
            {emotions}

            Risk level:
            {risk_level}

            Explain in 3-4 sentences why this text may emotionally manipulate readers.
            Focus on emotional language, fear triggers, outrage framing, or urgency tactics.
            Be objective and analytical.
            """

    response = model.generate_content(prompt)

    return response.text