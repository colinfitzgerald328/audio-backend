This is a simple backend server deployed on kubernetes that exposes an API to transcribe audio files into text. Currently, I'm testing via arbitrage whether it is cheaper to self-host the OpenAI Whisper model, or just use the API client. My theory is that at scale, self-hosting the model turns out to be cheaper.

You can try for yourself like so: 

Bash command: 

```bash
curl -X POST -F "file=@/path/to/your/audio/file.mp3" https://audio-backend-iyuk3izvyq-uc.a.run.app/transcribe
```

Python script: 

```python
import requests

# Replace '/path/to/your/audio/file.mp3' with the actual path to your audio file
file_path = '/path/to/your/audio/file.mp3'

# URL of the transcription API endpoint
transcribe_url = 'https://audio-backend-iyuk3izvyq-uc.a.run.app/transcribe'

# Create a dictionary with the file to be uploaded
files = {'file': open(file_path, 'rb')}

# Send a POST request to the transcription API endpoint
response = requests.post(transcribe_url, files=files)

# Print the response from the API
print(response.json())
```
