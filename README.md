
### 📘 `README.md`

```markdown
# Real-Time Caption Generation for Visually Impaired

A Python-based AI vision assistant designed to help visually impaired individuals perceive and understand their surroundings through real-time audio descriptions. The system leverages cutting-edge models like BLIP, CLIP, and EasyOCR to convert visual data into speech using natural language understanding and computer vision.

## 🧠 Features

- 🎥 Real-time video feed processing via webcam.
- 🗣️ Voice command interaction using SpeechRecognition.
- 👁️ Object recognition using OpenAI’s CLIP.
- 📄 Scene and question answering with Salesforce BLIP.
- 🔤 Text detection using EasyOCR.
- 🔊 Spoken output with pyttsx3 (offline TTS).
- ⚙️ Modular, thread-safe architecture with auto-captioning.

## 🔧 System Architecture

1. **Video Input** – Captured via OpenCV.
2. **Voice Input** – Captured and transcribed using SpeechRecognition.
3. **Processing Pipeline**
   - CLIP → Object Recognition
   - BLIP → Visual Question Answering
   - EasyOCR → Text Detection
4. **Output** – Delivered as spoken audio using pyttsx3.
5. **Multithreaded** – Handles camera, speech synthesis, and recognition concurrently.
```
## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/exoexo-1/Real-Time-Caption-Generation-for-Visually-Impaired.git
cd Real-Time-Caption-Generation-for-Visually-Impaired
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Model Weights

Ensure you have:
- CLIP (from OpenAI): https://github.com/openai/CLIP
- BLIP (HuggingFace): https://huggingface.co/Salesforce/blip-vqa-capfilt-large

You can load these directly via `transformers` and `torch`.

### 5. Run the Application

```bash
jupyter notebook visual_echo.ipynb
```

## 🖥️ Requirements

- Python 3.8+
- Webcam & Microphone
- Optional: GPU for faster inference (recommended for BLIP)


## 🚀 Future Enhancements

- 🔲 Bounding box support for object localization.
- 🔊 Offline speech recognition engine.
- 📱 Mobile and edge deployment (Jetson Nano / Raspberry Pi).
- 🔁 Personalized user profiles and interaction history.
- 🧠 Integration with LLaVA for richer multimodal interaction.

## 🙏 Acknowledgements

- [OpenAI CLIP](https://github.com/openai/CLIP)
- [Salesforce BLIP](https://huggingface.co/Salesforce/blip-vqa-capfilt-large)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [OpenCV](https://pypi.org/project/opencv-python/)

---

© 2025 – Lakshya Agrawal, Soumil Jain, Mahi Pahuja, Ishaan Kaul
```

