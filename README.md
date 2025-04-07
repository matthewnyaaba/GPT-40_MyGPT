# Nyaaba's GenAI-ERA Assistant (GPT-4o Powered)

This is a personal AI assistant built using GPT-4o via OpenAI API. It supports text-based chat with future plans to add voice, vision, and multilingual African support.

## 🔧 Features
- GPT-4o assistant
- Flask + OpenAI API
- Render-hosted deployment
- Plans for vision, audio, and multilingual extensions

## 🧪 Try It Live
[🔗 Your Render URL Here]

## ⚙️ Tech Stack
- Python (Flask)
- OpenAI API (GPT-4o)
- HTML + JS
- Render (Deployment)

## 🚀 Getting Started Locally
```bash
git clone https://github.com/matthewnyaaba/GPT-40_MyGPT.git
cd GPT-40_MyGPT
pip install -r requirements.txt

Absolutely! Below is the full README text in a single plain-text block you can easily copy and paste into your project folder as README.md — or save it in a text file before zipping:

yaml
Copy
Edit
# 🌍 GenAI-ERA Multimodal Assistant

**A lightweight, multimodal AI assistant powered by OpenAI's GPT-4o, built with Flask.**  
This app allows users to interact using **text** or **voice input**, supports **multilingual prompts**, and returns intelligent responses using GPT-4o's latest capabilities. Built as part of the AI4STEM and GenAI-ERA initiatives, this project promotes accessible AI for education and global communication.

---

## 🧠 What It Does

- Accepts **text** and **speech input** via microphone
- Communicates with **OpenAI's GPT-4o** for intelligent responses
- Supports **language selection** for multilingual interaction (extension-ready)
- Returns responses to the user interface in real-time
- Clean and minimal design using HTML, JavaScript, and Flask backend

---

## 📸 Screenshot

![GenAI-ERA Screenshot](static/screenshot.png)

---

## ⚙️ Installation & Running Locally

> Make sure Python 3.11+ is installed on your system.

### 1. Clone the Repository

git clone https://github.com/matthewnyaaba/GPT-40_MyGPT.git cd GPT-40_MyGPT

shell
Copy
Edit

### 2. Create Virtual Environment (optional but recommended)

python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate

shell
Copy
Edit

### 3. Install Dependencies

pip install -r requirements.txt

less
Copy
Edit

### 4. Setup Environment Variables

Create a `.env` file and add your [OpenAI API key](https://platform.openai.com/account/api-keys):

OPENAI_API_KEY=sk-xxxxx-your-api-key-here

yaml
Copy
Edit

---

### 5. Run the App

python app.py

arduino
Copy
Edit

Visit: `http://127.0.0.1:5000` in your browser.

---

## 🔊 Using GPT-4o Multimodal Capabilities

This project uses the `gpt-4o` model via the OpenAI API to:

- Accept and process **text** input from users
- Accept **speech input** (browser microphone via Web API)
- Return responses via OpenAI’s `chat.completions.create()` endpoint
- (Optionally extensible) Vision/audio input can be added using OpenAI's tools or Whisper/DALL·E integration

### Backend: `app.py`

```python
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_message}]
    )
    return jsonify({"reply": completion.choices[0].message.content})
🖼️ Frontend Highlights
HTML: templates/index.html
html
Copy
Edit
<textarea id="promptInput" placeholder="Type your message..."></textarea>
<button onclick="sendPrompt()">Send</button>
<button onclick="startRecording()">🎤 Start Recording</button>
JavaScript: static/script.js
javascript
Copy
Edit
function sendPrompt() {
    const message = document.getElementById("promptInput").value;
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("responseBox").innerText = data.reply;
    });
}
📂 Project Structure
bash
Copy
Edit
GPT-40_MyGPT/
│
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── .env                 # Your OpenAI key (not public!)
├── templates/
│   └── index.html       # Web page
├── static/
│   ├── script.js        # Frontend logic
│   └── screenshot.png   # UI Screenshot (optional)
└── README.md            # This file
🌐 Deployment
This app is fully deployable on platforms like Render, Railway, or Replit:

For Render:

Connect your GitHub repo

Add OPENAI_API_KEY under Environment Variables

Set the build/run command to:

nginx
Copy
Edit
pip install -r requirements.txt && python app.py
🙌 Credits
Developed by Matthew Nyaaba as part of the GenAI-ERA initiative.
Inspired by the mission to make multimodal AI tools more accessible to educators, learners, and researchers globally.

📃 License
This project is open-source and licensed under the MIT License.

yaml
Copy
Edit

---

Let me know if you
python app.py
