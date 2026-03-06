from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from app.gemini_service import generate_explanation

app = FastAPI(title="Media Guard API")

# ---------------------------
# Load Models
# ---------------------------

single_emotion_classifier = pipeline(
    "text-classification",
    model="./backend/models/emotion_model_single",
    top_k=None
)

goemotion_classifier = pipeline(
    "text-classification",
    model="./backend/models/emotion_model_goemotions",
    top_k=None
)

# ---------------------------
# Label Mapping (Single Model)
# ---------------------------

SINGLE_LABEL_MAP = {
    "LABEL_0": "sadness",
    "LABEL_1": "joy",
    "LABEL_2": "love",
    "LABEL_3": "anger",
    "LABEL_4": "fear",
    "LABEL_5": "surprise"
}

# ---------------------------
# GoEmotions Label Mapping
# ---------------------------

GOEMOTION_LABEL_MAP = {
0: "admiration",
1: "amusement",
2: "anger",
3: "annoyance",
4: "approval",
5: "caring",
6: "confusion",
7: "curiosity",
8: "desire",
9: "disappointment",
10: "disapproval",
11: "disgust",
12: "embarrassment",
13: "excitement",
14: "fear",
15: "gratitude",
16: "grief",
17: "joy",
18: "love",
19: "nervousness",
20: "optimism",
21: "pride",
22: "realization",
23: "relief",
24: "remorse",
25: "sadness",
26: "surprise",
27: "neutral"
}

# ---------------------------
# Request Schema
# ---------------------------

class TextInput(BaseModel):
    text: str
    model_type: str


# ---------------------------
# Improved Risk Scoring
# ---------------------------

def compute_risk_score(emotions):

    extreme_risk = [
        "fear", "anger", "disgust",
        "grief", "nervousness", "sadness"
    ]

    manipulation_signals = [
        "surprise", "annoyance", "disappointment"
    ]

    positive = [
        "joy", "love", "gratitude", "optimism"
    ]

    score = 0.0

    # Strong emotional triggers
    for e in extreme_risk:
        score += emotions.get(e, 0) * 0.8

    # Manipulative amplification
    for e in manipulation_signals:
        score += emotions.get(e, 0) * 0.5

    # Positive emotions reduce manipulation
    for e in positive:
        score -= emotions.get(e, 0) * 0.4

    risk_score = max(0, min(100, score * 100))

    if risk_score <= 35:
        level = "Low"
    elif risk_score <= 65:
        level = "Medium"
    else:
        level = "High"

    return round(risk_score, 2), level


# ---------------------------
# Routes
# ---------------------------

@app.get("/")
def home():
    return {"status": "Media Guard backend is running 🚀"}


@app.post("/analyze")
def analyze_text(payload: TextInput):

    text = payload.text
    model_type = payload.model_type.lower()

    if not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    # -----------------------
    # BASIC MODEL
    # -----------------------

    if model_type == "basic":

        results = single_emotion_classifier(text)
        scores = results[0]

        emotion_scores = {
            SINGLE_LABEL_MAP.get(item["label"], item["label"]): float(item["score"])
            for item in scores
        }

        model_used = "Single Label Emotion Model"

    # -----------------------
    # ADVANCED MODEL
    # -----------------------

    elif model_type == "advanced":

        results = goemotion_classifier(text)
        scores = results[0]

        emotion_scores = {}

        for item in scores:

            raw_label = item["label"]

            if raw_label.startswith("LABEL_"):
                idx = int(raw_label.split("_")[1])
                label_name = GOEMOTION_LABEL_MAP.get(idx, raw_label)
            else:
                label_name = raw_label

            emotion_scores[label_name] = float(item["score"])

        model_used = "GoEmotions Multi-Label Model"

    else:
        raise HTTPException(status_code=400, detail="Invalid model_type")

    # -----------------------
    # Compute Risk
    # -----------------------

    risk_score, risk_level = compute_risk_score(emotion_scores)
    explanation = generate_explanation(text,emotion_scores,risk_level)

    return {
        "text": text,
        "model_used": model_used,
        "emotions": emotion_scores,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "explanation": explanation
    }