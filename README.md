# 🎭 Real-Time Emotion Detector Web App

A real-time **Emotion Detection App** that supports **text** and **speech input**, powered by a **transformer model**, capable of detecting **27 fine-grained emotions** and visualizing results with **emojis** and **confidence charts**. Built using **Streamlit** for an interactive UI and Hugging Face's **DistilBERT emotion model**.

---

## 🚀 Demo Preview

![image](https://github.com/user-attachments/assets/b7fca025-4a02-4e39-a658-20a434603a63)


## 📌 Features

- 🔠 **Text-based Emotion Detection**
- 🎙️ **Speech-based Emotion Detection (Real-Time)**
- 🤖 **27 Emotion Labels using Transformer Model**
- 📊 **Confidence Score Bar Chart for All Emotions**
- 😀 **Emoji Output for Detected Emotion**
- ⚡ **Fast and Responsive with Streamlit**
- 💬 **Clear UI with Tabs for Text & Speech Modes**

---

## 🧠 Model Used

- **Model**: [`distilbert-base-uncased-emotion`](https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion)
- **Source**: Hugging Face Transformers
- **Emotions Covered** (27 total):  
  `admiration`, `amusement`, `anger`, `annoyance`, `approval`, `caring`, `confusion`, `curiosity`, `desire`, `disappointment`, `disapproval`, `disgust`, `embarrassment`, `excitement`, `fear`, `gratitude`, `grief`, `joy`, `love`, `nervousness`, `optimism`, `pride`, `realization`, `relief`, `remorse`, `sadness`, `surprise`

---

## 📦 Installation

### 🛠️ Install Dependencies

Example packages used:

streamlit

transformers

torch

SpeechRecognition

pyaudio (for microphone support)

emotion-detector/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
├── README.md             # Project description

📸 Sample Outputs
Text Input
Input: "I just got promoted!"
Output:
Emotion: joy 😊
Confidence: 93.4%

Speech Input
Spoken: "I’m feeling really sad today."
Output:
Emotion: sadness 😢
Confidence: 88.1%

💡 Future Improvements
🌍 Multilingual emotion detection

📱 Mobile-friendly layout

🧩 Emotion timeline history tracking

🌐 Deployment on cloud platforms (e.g., Streamlit Cloud or Hugging Face Spaces)

🙋‍♂️ Author
Vineet Rathod
B.Tech (IT) | 7th Semester
Project developed during Internship for Final Year Submission

📄 License
This project is licensed under the MIT License.

⭐ Show Your Support
If you like this project, feel free to ⭐ the repository or fork it to build your own emotion-based applications!
