from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k = None
)

text = "Breaking news! This is terrifying and shocking."

results = emotion_classifier(text)

print("Emotion scores: \n")
for item in results[0]:
    print(item["label"], ":", round(item["score"], 4))