import streamlit as st
st.set_page_config(page_title="🎭 Emotion Detector", layout="centered")
import speech_recognition as sr
from transformers import pipeline

# ----------------------------
# Emotion to emoji mapping
# ----------------------------
EMOJI_MAP = {
    "admiration": "😍", "amusement": "😂", "anger": "😠", "annoyance": "😒",
    "approval": "👍", "caring": "🤗", "confusion": "😕", "curiosity": "🧐",
    "desire": "😋", "disappointment": "😞", "disapproval": "👎", "disgust": "🤢",
    "embarrassment": "😳", "excitement": "🤩", "fear": "😨", "gratitude": "🙏",
    "grief": "😭", "joy": "😄", "love": "❤️", "nervousness": "😬",
    "optimism": "😊", "pride": "😌", "realization": "💡", "relief": "😌",
    "remorse": "😔", "sadness": "😢", "surprise": "😲", "neutral": "😐"
}

# ----------------------------
# Load emotion model
# ----------------------------
@st.cache_resource
def load_emotion_model():
    return pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=True)

model = load_emotion_model()

# ----------------------------
# Streamlit Page Setup
# ----------------------------

st.title("🎭 27-Emotion Detector (Text + Speech + Emojis)")

tab1, tab2 = st.tabs(["📝 Text Input", "🎤 Speech Input"])

# ----------------------------
# Text Input Tab
# ----------------------------
with tab1:
    st.subheader("📝 Type a sentence")
    user_input = st.text_area("Enter your sentence here:")

    if st.button("Detect Emotion", key="text_btn"):
        if user_input.strip() == "":
            st.warning("Please type something.")
        else:
            results = model(user_input)[0]
            sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
            top_emotion = sorted_results[0]
            emoji = EMOJI_MAP.get(top_emotion['label'].lower(), "❓")
            st.success(f"Top Emotion: {emoji} **{top_emotion['label'].capitalize()}** ({top_emotion['score']:.2f})")

            st.markdown("### 🔎 Full Emotion Breakdown:")
            for r in sorted_results:
                emoji = EMOJI_MAP.get(r['label'].lower(), "❓")
                st.write(f"{emoji} **{r['label'].capitalize()}**: {r['score']:.2f}")

# ----------------------------
# Speech Input Tab
# ----------------------------
with tab2:
    st.subheader("🎤 Speak to detect emotion")

    if st.button("Start Recording", key="speech_btn"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("🎙 Listening... Please speak now.")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                st.write("📝 **Recognized Text:**", text)

                results = model(text)[0]
                sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
                top_emotion = sorted_results[0]
                emoji = EMOJI_MAP.get(top_emotion['label'].lower(), "❓")
                st.success(f"Top Emotion: {emoji} **{top_emotion['label'].capitalize()}** ({top_emotion['score']:.2f})")

                st.markdown("### 🔎 Full Emotion Breakdown:")
                for r in sorted_results:
                    emoji = EMOJI_MAP.get(r['label'].lower(), "❓")
                    st.write(f"{emoji} **{r['label'].capitalize()}**: {r['score']:.2f}")

            except sr.UnknownValueError:
                st.error("❌ Could not understand your speech.")
            except sr.RequestError as e:
                st.error(f"❌ Could not request results from Google: {e}")
