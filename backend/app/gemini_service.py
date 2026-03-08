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

def rewrite_neutral(text):
    

    prompt = f"""
                PERSONA
                You are a media literacy AI assistant that specializes in rewriting emotionally manipulative media content into clear, neutral, and responsible communication.

                Your goal is to help readers understand information without unnecessary emotional pressure or psychological distress.

                CONTEXT
                Some media content uses emotionally charged language such as fear amplification, outrage framing, sensational wording, or urgency triggers. 
                These techniques can influence readers emotionally rather than informing them objectively.

                The system needs to transform such content into a neutral and mentally safe version while preserving the original factual meaning.

                INPUT TEXT
                {text}

                TASK
                Rewrite the text so that it becomes neutral, balanced, and informative.

                The rewritten version should:
                • Remove emotionally manipulative language
                • Eliminate sensational or alarmist phrasing
                • Avoid fear-inducing or panic-driven wording
                • Reduce exaggerated claims or dramatic framing
                • Preserve the factual information and core message

                REWRITING GUIDELINES
                • Use calm, objective, and informative language
                • Replace emotionally charged words with neutral alternatives
                • Maintain clarity and readability
                • Avoid adding new opinions or interpretations
                • Keep the meaning of the original information intact

                MENTAL WELL-BEING GOAL
                The rewritten text should support healthy information consumption by:
                • Reducing panic or emotional escalation
                • Preventing unnecessary anxiety
                • Encouraging calm and rational understanding

                OUTPUT FORMAT
                Provide only the rewritten text in a clear and neutral tone.

                NEUTRAL REWRITTEN VERSION:
                """
    response = model.generate_content(prompt)
    return response.text
