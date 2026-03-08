import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

def calculate_emotional_intensity(emotions):

    risk_emotions = [
        "fear",
        "anger",
        "sadness",
        "disgust",
        "nervousness"
    ]

    intensity = 0

    for e in risk_emotions:
        intensity += emotions.get(e, 0)

    return intensity

st.set_page_config(page_title="Media Guard", layout="centered")

st.title("🛡️ Media Guard – Emotion Detection")
st.write("Analyze emotional tone in news and social media content.")

user_text = st.text_area("Enter text")

model_type = st.selectbox(
    "Select Emotion Model",
    ["basic", "advanced"]
)

if st.button("Analyze Emotion"):
    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            res = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={
                    "text": user_text,
                    "model_type": model_type
                }
            )

            if res.status_code != 200:
                st.error(f"Backend Error: {res.text}")
            else:
                data = res.json()

                st.subheader(f"Model Used: {data['model_used']}")

                # -------------------------------
                # Show Top 5 Emotions Only
                # -------------------------------

                emotions = data["emotions"]

                top_emotions = dict(
                    sorted(
                        emotions.items(),
                        key=lambda x: x[1],
                        reverse=True
                    )[:5]
                )

                st.subheader("Top Emotion Scores")
                st.bar_chart(top_emotions)

                # -------------------------------
                # Dominant Emotion
                # -------------------------------

                top_emotion = max(
                    emotions,
                    key=emotions.get
                )

                st.info(f"🔎 Dominant emotion: **{top_emotion}**")

                # -------------------------------
                # Manipulation Risk
                # -------------------------------

                st.subheader("Manipulation Risk")

                st.metric(
                    "Risk Score",
                    f"{data['risk_score']} / 100"
                )

                st.subheader("Detected Persuasion Patterns")

                patterns = data["persuasion_patterns"]

                if patterns:
                    for p in patterns:
                        st.warning(f"⚠️ {p}")
                else:
                    st.success("No strong persuasion patterns detected.")

                risk = data["risk_level"]

                if risk == "High":
                    st.error(f"Risk Level: {risk}")
                elif risk == "Medium":
                    st.warning(f"Risk Level: {risk}")
                else:
                    st.success(f"Risk Level: {risk}")

                if data["risk_level"] == "High":
                    st.error("⚠️ This content appears highly emotionally manipulative.")
                elif data["risk_level"] == "Medium":
                    st.warning("⚠️ This content shows moderate emotional manipulation.")
                else:
                    st.success("✅ This content appears emotionally neutral or safe.")

                st.subheader("AI Explanation")

                st.write(data["explanation"])

                if data["neutral_rewrite"]:

                    st.subheader("Neutral Rewrite")

                    st.success(data["neutral_rewrite"])

                    original_intensity = calculate_emotional_intensity(data["emotions"])

                    rewrite_text = data["neutral_rewrite"]

                    rewrite_res = requests.post(
                        "http://127.0.0.1:8000/analyze",
                        json={
                            "text": rewrite_text,
                            "model_type": model_type
                        }
                    )

                    rewrite_data = rewrite_res.json()

                    rewrite_intensity = calculate_emotional_intensity(
                        rewrite_data["emotions"]
                    )

                    st.subheader("Emotional Intensity Comparison")

                    chart_data = pd.DataFrame(
                        {
                            "Text Type": ["Original Text", "Neutral Rewrite"],
                            "Emotional Intensity": [
                                original_intensity,
                                rewrite_intensity
                            ]
                        }
                    )

                    emotion_labels = list(top_emotions.keys())

                    original_scores = [
                        emotions.get(e, 0) * 100 for e in emotion_labels
                    ]

                    rewrite_scores = [
                        rewrite_data["emotions"].get(e, 0) * 100 for e in emotion_labels
                    ]

                    fig, ax = plt.subplots()

                    x = range(len(emotion_labels))
                    width = 0.35

                    ax.bar(
                        [i - width/2 for i in x],
                        original_scores,
                        width,
                        label="Original Text"
                    )

                    ax.bar(
                        [i + width/2 for i in x],
                        rewrite_scores,
                        width,
                        label="Neutral Rewrite"
                    )

                    ax.set_xlabel("Emotion Type")
                    ax.set_ylabel("Emotion Score")
                    ax.set_title("Emotion Intensity: Original vs Neutral Rewrite")

                    ax.set_xticks(x)
                    ax.set_xticklabels([e.capitalize() for e in emotion_labels])

                    ax.legend()

                    st.pyplot(fig)

        except Exception as e:
            st.error(f"Connection Error: {str(e)}")