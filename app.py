import os
from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("message")
    language = data.get("language", "English")
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. Reply in {language}."},
                {"role": "user", "content": prompt}
            ]
        )
        return jsonify({"reply": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    audio = request.files["audio"]
    try:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio
        )
        return jsonify({"text": transcript.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/speak", methods=["POST"])
def speak():
    data = request.json
    text = data.get("text")
    try:
        speech = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=text
        )
        output_path = "static/output.mp3"
        with open(output_path, "wb") as f:
            f.write(speech.content)
        return jsonify({"audio_url": "/static/output.mp3"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
