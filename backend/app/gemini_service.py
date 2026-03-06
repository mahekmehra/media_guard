import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_explanation(text, emotions, risk_level):

    prompt = f"""
            ROLE
            You are a media literacy AI assistant trained to analyze emotional manipulation in news, social media, and online content. 
            Your explanations should be calm, neutral, and educational so that readers can understand the manipulation without feeling judged.

            CONTEXT
            The system has analyzed a piece of text and detected emotional signals that may indicate manipulation.
            These signals include detected emotions and a calculated manipulation risk level.

            INPUT DATA
            Text Content:
            {text}

            Detected Emotions:
            {emotions}

            Risk Level:
            {risk_level}

            TASK
            Analyze the text and explain why it may emotionally manipulate readers.

            Focus on identifying:
            - Emotionally charged language
            - Fear-based or outrage-driven framing
            - Urgency or panic triggers
            - Exaggeration or sensational tone
            - Language designed to provoke strong reactions rather than inform

            EXPLANATION GUIDELINES
            - Write in a calm, patient, and objective tone.
            - Avoid accusing the author directly.
            - Frame the explanation as an analysis of communication style.
            - Help the reader understand *how* emotional influence may occur.

            OUTPUT FORMAT
            Provide a short human-readable explanation in **3–4 sentences** that clearly explains:
            1. The emotional signals present in the text
            2. How these signals could influence readers
            3. Why the content may be considered emotionally manipulative

            EXPLANATION:
            """


    response = model.generate_content(prompt)

    return response.text