# 🌐 Real-Time Language Translator Using Neural Machine Translation (NMT)

A web-based application that provides real-time **text and voice translation** between multiple languages (English, Hindi, Russian and other European languages) using **Neural Machine Translation (NMT)** models from Helsinki-NLP and Hugging Face Transformers.

---

## 🚀 Features

- 🔁 Bidirectional translation: Between languages such as English, Hindi, Russian and European languages
- 🧠 NMT-based translation using MarianMT (Helsinki-NLP)
- 🎤 Speech-to-text input using Web Speech API
- 🔊 Text-to-speech output for translated text
- 🌍 Simple and responsive UI using HTML, CSS, JS
- 🧩 Backend built with Python & Django

---

## 🧠 Model Details

- **Transformer**: MarianMT by [Helsinki-NLP](https://huggingface.co/Helsinki-NLP)
- **Translation direction**:  Between languages such as English, Hindi, Russian and European languages
- **Model provider**: [Hugging Face Transformers](https://huggingface.co/models?search=Helsinki-NLP)

Example models used:
- `Helsinki-NLP/opus-mt-en-hi`
- `Helsinki-NLP/opus-mt-en-de`
- `Helsinki-NLP/opus-mt-en-ru`
- And reverse models like `opus-mt-hi-en`, etc.

---

## ⚙️ Setup Instructions

### 1. 🐍 Create a Virtual Environment
python -m venv myenv
#### Activate:
- Windows:
  myenv\Scripts\activate
- macOS/Linux:
  source myenv/bin/activate

### 2. 📦 Install Dependencies
pip install django transformers torch sentencepiece

### 3. 🛠️ Run Migrations
python manage.py migrate

### 4. 🔥 Start the Development Server
python manage.py runserver <br>
Now visit http://127.0.0.1:8000 in your browser.

---

## 🖥️ Frontend
- HTML/CSS for layout and design
- JavaScript (Web Speech API) for microphone and speaker integration
- AJAX for async requests to the backend

## 🧰 Tech Stack
- 🧠 Hugging Face Transformers (MarianMT models)
- 🌐 Django (Backend)
- 🎤 Web Speech API (Speech-to-Text and Text-to-Speech)
- 🗄️ SQLite (Lightweight storage)

## 🙌 Author
- 👤 Poojith L
- 📫 Reach out on [LinkedIn](https://www.linkedin.com/in/poojithl) or check out more projects on [GitHub](https://github.com/Poojith-L)
