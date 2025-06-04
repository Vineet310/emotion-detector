import streamlit as st
import speech_recognition as sr
from transformers import pipeline
import time

st.set_page_config(page_title="🎤 Real-Time Speech Emotion Detector", layout="centered")

@st.cache_resource
def load_model():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

model = load_model()

st.title("🎤 Real-Time Speech-to-Emotion Detector")

recognizer = sr.Recognizer()

if st.button("🎙️ Start Recording"):
    with st.spinner("Listening..."):
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            st.info("Please speak now...")
            audio = recognizer.listen(source, timeout=5)
        
        try:
            st.success("Processing speech...")
            text = recognizer.recognize_google(audio)
            st.write("📝 **Recognized Text:**", text)
            
            result = model(text)[0]
            top_emotion = max(result, key=lambda x: x["score"])
            st.markdown(f"### 😃 Detected Emotion: **{top_emotion['label'].upper()}** (Confidence: {top_emotion['score']:.2f})")

        except sr.UnknownValueError:
            st.error("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
