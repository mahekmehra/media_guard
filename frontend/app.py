import streamlit as st
import requests

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

                st.write(f"Risk Level: **{data['risk_level']}**")

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

        except Exception as e:
            st.error(f"Connection Error: {str(e)}")