import whisper
import tempfile

model = whisper.load_model("base")


def transcribe(audio_file):
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_audio_file:
        temp_audio_path = temp_audio_file.name
        # Save the audio file to the temporary path
        audio_file.save(temp_audio_path)

    result = model.transcribe(temp_audio_path)
    return result["text"]
