# 🛡️ Media Guard – AI System for Emotional Manipulation Detection

Media Guard is an AI-powered system that detects emotional manipulation in news and social media content using machine learning, natural language processing, and generative AI.

The system analyzes emotional tone, detects persuasion tactics, explains manipulation patterns, and rewrites emotionally manipulative text into neutral language.

---

# 🚀 Key Features

## 🧠 Dual Emotion Detection Models

Users can analyze text using two different emotion models.

### Basic Emotion Model

Fine-tuned DistilBERT classifier trained on emotion datasets.

Detects:

- sadness
- joy
- love
- anger
- fear
- surprise

### Advanced Emotion Model

Fine-tuned GoEmotions dataset supporting multi-label emotion detection with **28 emotion categories**.

Provides deeper emotional context and nuanced analysis.

---

# ⚠️ Manipulation Risk Detection

The system calculates a **Manipulation Risk Score (0–100)** based on detected emotional signals.

| Score | Level |
|------|------|
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

Media Guard detects common emotional persuasion techniques used in media.

| Pattern | Description |
|-------|-------------|
| Fear Bait | Creates panic or danger perception |
| Outrage Bait | Provokes anger or moral outrage |
| Sympathy Bait | Exploits sadness or suffering |
| Urgency Bait | Pressures immediate action |
| Sensationalism | Uses exaggerated dramatic language |

### Example Output

```
⚠ Fear Bait
⚠ Urgency Bait
⚠ Sensationalism
```

---

# 🤖 AI Explanation Engine (Gemini)

The system integrates **Google Gemini** to explain why content may be emotionally manipulative.

### Example Explanation

```
The text uses catastrophic language such as "destroy everything"
and "panic is spreading", which amplifies fear and urgency.
Such framing can emotionally manipulate readers by triggering
panic rather than presenting balanced information.
```

---

# ✏️ Neutral Rewrite Engine

Media Guard can rewrite emotionally manipulative text into **neutral, balanced language**.

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

The system visualizes emotional intensity in the analyzed text.

### Features

- Top-5 detected emotions
- Emotion comparison graph
- Original vs neutral rewrite comparison

Example visualization:

```
Emotion Intensity: Original vs Neutral Rewrite
```

This demonstrates how the neutral rewrite reduces emotional manipulation intensity.

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
Emotion Visualization Dashboard
```

---

# 🧰 Tech Stack

## Backend

- FastAPI
- Python

## Frontend

- Streamlit

## Machine Learning

- HuggingFace Transformers
- DistilBERT
- GoEmotions Dataset
- PyTorch

## Generative AI

- Google Gemini API

## Data Visualization

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
└── README.md
```

---

# ⚙️ Installation

## Clone the repository

```
git clone https://github.com/YOUR_USERNAME/media_guard.git
cd media_guard
```

## Install dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create `.env` inside **backend directory**:

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

### Persuasion Patterns

```
⚠ Fear Bait
⚠ Urgency Bait
```

### AI Explanation

```
The text uses catastrophic language that amplifies fear and urgency.
```

### Neutral Rewrite

```
Authorities reported a developing situation and are assessing risks.
```

---

# 🗺️ Project Roadmap

## Completed Phases

| Phase | Feature |
|------|--------|
| 1 | Emotion Detection Models |
| 2 | Manipulation Risk Scoring |
| 3 | Gemini AI Explanation |
| 4 | Neutral Rewrite Engine |
| 5 | Persuasion Pattern Detection |
| 6 | Emotion Visualization Dashboard |

---

## Upcoming Phases

### Phase 9 — Emotion Timeline Analysis
Detect emotional escalation across multi-paragraph text.

### Phase 7 — PDF AI Analysis Report
Generate downloadable AI reports with charts and analysis.

### Phase 8 — Browser Extension
Analyze emotional manipulation directly on webpages.

### Phase 10 — Cloud Deployment
Deploy backend and frontend with live demo access.

---

# 🔮 Future Enhancements

## React Frontend
Replace Streamlit with a modern **React UI** for improved performance and scalability.

## Docker Deployment
Containerize backend and frontend using **Docker** and deploy to cloud platforms such as **AWS** or **GCP**.

---

# 👩‍💻 Author

**Mahek Mehra**

Machine Learning / Generative AI Project
