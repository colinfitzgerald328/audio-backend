from flask import Flask, request
from flask_cors import CORS
import functions 


app = Flask(__name__)
CORS(app)


@app.route("/")
def server_status():
    return "Server is operational"


@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    audio_file = request.files["file"]
    transcription = functions.transcribe(audio_file)
    return {
        "operation": "success",
        "transcription": transcription
    }


if __name__ == "__main__":
    app.run(host="127.0.0.1")
