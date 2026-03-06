# 🛡️ Media Guard – AI System for Emotional Manipulation Detection

Media Guard is an AI-powered system that detects emotional manipulation in news and social media content.

It combines Machine Learning emotion detection with Generative AI explanations to help users understand how emotionally persuasive content works.

---

# 🚀 Features

## 🧠 Dual Emotion Detection Models

Users can choose between:

### Basic Emotion Model
- Fine-tuned DistilBERT
- Single-label classification
- Fast inference

### Advanced Emotion Model
- Fine-tuned GoEmotions dataset
- Multi-label emotion detection
- More nuanced emotional analysis

---

# ⚠️ Emotional Manipulation Detection

The system calculates a **Manipulation Risk Score** based on detected emotions.

## Risk Levels

| Score | Level |
|------|------|
| 0–35 | Low |
| 36–65 | Medium |
| 66–100 | High |

---

## High-Risk Emotions

These emotions increase manipulation risk:

- fear
- anger
- disgust
- grief
- nervousness
- sadness

---

## Manipulation Signals

These emotions may indicate persuasive framing:

- surprise
- annoyance
- disappointment

---

## Positive Emotions (Reduce Risk)

Positive emotions decrease the manipulation score:

- joy
- love
- gratitude
- optimism

---

# 🤖 AI Explanation Engine (Gemini)

Using **Google Gemini**, the system explains why content may be emotionally manipulative.

### Example Output

**Detected emotions**

```
fear (0.92), surprise (0.05)
```

**Risk Level**

```
High
```

**AI Explanation**

```
This text uses catastrophic language such as "destroy everything"
and "panic is spreading", which amplifies fear and urgency in
readers. Such framing can emotionally manipulate audiences by
triggering panic rather than presenting balanced information.
```

---

# 🏗️ System Architecture

```
User Input
   ↓
Streamlit Frontend
   ↓
FastAPI Backend
   ↓
Emotion Detection Model
   ↓
Manipulation Risk Engine
   ↓
Gemini AI Explanation
   ↓
Results Display
```

---

# 🧰 Tech Stack

## Backend

- FastAPI
- Transformers (HuggingFace)
- Python

## Frontend

- Streamlit

## Machine Learning

- DistilBERT (fine-tuned)
- GoEmotions dataset
- PyTorch

## Generative AI

- Google Gemini API

---

# 📂 Project Structure

```
media_guard/
│
├── backend
│   └── app
│       ├── main.py
│       ├── gemini_service.py
│
├── frontend
│   └── app.py
│
├── experiments
│   └── emotion_model_test.py
│
├── models
│   └── (not included in repo)
│
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/media_guard.git
cd media_guard
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create `.env` inside **backend** directory.

```
GEMINI_API_KEY=your_api_key
```

---

# ▶️ Run Backend

```
uvicorn backend.app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend

```
streamlit run frontend/app.py
```

---

# 🧪 Example Input

```
Breaking news! A catastrophic disaster is about to strike the city.
People are terrified and panic is spreading rapidly.
```

---

# 📊 Example Output

### Emotion Detection

```
fear: 0.92
nervousness: 0.14
surprise: 0.05
```

### Risk Score

```
82 / 100
High
```

### AI Explanation

```
The text uses catastrophic language that amplifies fear and urgency.
Such framing can emotionally manipulate readers by triggering panic.
```

---

# 🚀 Future Improvements

- Neutral rewrite of manipulative content
- Emotional persuasion pattern detection
- Article-level analysis
- RAG-based news verification
- Browser extension for real-time analysis

---

# 👩‍💻 Author

Mahek Mehra

AI / Machine Learning Project
