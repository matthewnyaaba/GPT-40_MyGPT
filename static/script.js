async function sendPrompt() {
  const prompt = document.getElementById("promptInput").value;
  const language = document.getElementById("languageSelect").value;
  const responseBox = document.getElementById("responseBox");

  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: prompt, language })
  });
  const data = await res.json();
  responseBox.textContent = data.reply;
  speakResponse(data.reply);
}

async function transcribeAudio(blob) {
  const formData = new FormData();
  formData.append("audio", blob, "audio.webm");

  const res = await fetch("/transcribe", { method: "POST", body: formData });
  const data = await res.json();
  if (data.text) {
    document.getElementById("promptInput").value = data.text;
    sendPrompt();
  }
}

function speakResponse(text) {
  fetch("/speak", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  })
  .then(res => res.json())
  .then(data => {
    const audio = new Audio(data.audio_url);
    audio.play();
  });
}

let mediaRecorder;
let audioChunks = [];
function startRecording() {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      mediaRecorder = new MediaRecorder(stream);
      mediaRecorder.start();
      mediaRecorder.ondataavailable = e => audioChunks.push(e.data);
      mediaRecorder.onstop = () => {
        const blob = new Blob(audioChunks, { type: "audio/webm" });
        transcribeAudio(blob);
        audioChunks = [];
      };
    });
}

function stopRecording() {
  if (mediaRecorder) mediaRecorder.stop();
}
