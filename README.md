# 🛡️ Media Guard – AI System for Emotional Manipulation Detection

Media Guard is an AI-powered system that detects and analyzes emotional manipulation in news and social media content.

The system combines Machine Learning emotion detection with Generative AI reasoning and rewriting to help users understand and neutralize emotionally manipulative messaging.

---

# 🚀 Features

## 🧠 Dual Emotion Detection Models

Users can analyze text using two different emotion models:

### Basic Emotion Model

- Fine-tuned DistilBERT
- Single-label classification
- Faster inference
- 6 emotion categories

Supported emotions:

- sadness
- joy
- love
- anger
- fear
- surprise

### Advanced Emotion Model

- Fine-tuned GoEmotions dataset
- Multi-label emotion detection
- 28 emotion categories
- More nuanced emotional analysis

---

# ⚠️ Emotional Manipulation Detection

The system calculates a **Manipulation Risk Score (0–100)** based on detected emotions.

| Risk Score | Level |
|-----------|-------|
| 0–35 | Low |
| 36–65 | Medium |
| 66–100 | High |

### High-Risk Emotional Signals

- fear
- anger
- disgust
- grief
- nervousness
- sadness

### Positive Emotions (Reduce Risk)

- joy
- love
- gratitude
- optimism

---

# 🎯 Persuasion Pattern Detection

Media Guard identifies common emotional persuasion tactics used in media.

### Detected Patterns

| Pattern | Description |
|--------|-------------|
| Fear Bait | Uses fear to create panic or urgency |
| Outrage Bait | Attempts to provoke anger |
| Sympathy Bait | Exploits sadness or emotional suffering |
| Urgency Bait | Pushes immediate action through pressure |
| Sensationalism | Uses exaggerated dramatic language |

### Example Output

```
⚠️ Fear Bait
⚠️ Urgency Bait
⚠️ Sensationalism
```

---

# 🤖 AI Explanation Engine (Gemini)

Using **Google Gemini**, Media Guard explains why a piece of content may be emotionally manipulative.

### Example

**Detected emotions**

```
fear (0.92), surprise (0.05)
```

**Risk Level**

```
High
```

**Explanation**

```
The text uses catastrophic language such as "destroy everything"
and "panic is spreading", which amplifies fear and urgency in
readers. This framing may emotionally manipulate audiences by
triggering panic rather than presenting balanced information.
```

---

# ✏️ Neutral Rewrite Engine

Media Guard can rewrite emotionally manipulative content into **neutral, balanced language**.

### Original Text

```
This shocking disaster will destroy everything!
People are terrified and panic is spreading everywhere!
```

### Neutral Rewrite

```
Authorities reported a developing situation and are currently
assessing potential impacts while gathering further information.
```

---

# 📊 Emotional Intensity Dashboard

The system visualizes how emotional intensity changes after rewriting.

### Features

- Top-5 detected emotions
- Emotion comparison graph
- Original vs rewritten content

Example visualization:

```
Emotion Intensity: Original vs Neutral Rewrite
```

The dashboard shows that the neutral rewrite reduces emotional intensity.

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
Persuasion Pattern Detection
   ↓
Gemini AI Explanation
   ↓
Neutral Rewrite Generation
   ↓
Emotion Intensity Dashboard
```

---

# 🧰 Tech Stack

## Backend

- FastAPI
- Python
- Transformers (HuggingFace)

## Frontend

- Streamlit

## Machine Learning

- DistilBERT
- GoEmotions dataset
- PyTorch

## Generative AI

- Google Gemini API

## Visualization

- Matplotlib
- Pandas

---

# 📂 Project Structure

```
media_guard
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
│   └── (not included in repository)
│
├── .gitignore
├── requirements.txt
└── README.md

```

---

# ⚙️ Installation

## Clone Repository

```
git clone https://github.com/YOUR_USERNAME/media_guard.git
cd media_guard
```

## Install Dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create `.env` inside the **backend folder**.

```
GEMINI_API_KEY=your_api_key_here
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

### Persuasion Patterns

```
⚠️ Fear Bait
⚠️ Urgency Bait
```

### AI Explanation

```
The text uses catastrophic language that amplifies fear and urgency.
```

### Neutral Rewrite

```
Authorities reported a developing situation and are assessing potential impacts.
```

---

# 🚀 Upcoming Features

### Phase 7

- RAG-based news research assistant

### Phase 8

- Browser extension for real-time analysis

### Phase 9

- Downloadable AI analysis report (PDF)

---

# 👩‍💻 Author

**Mahek Mehra**

AI / Machine Learning Project
