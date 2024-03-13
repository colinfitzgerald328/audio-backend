This is a simple backend server deployed on kubernetes that exposes an API to transcribe audio files into text. Currently, I'm testing via arbitrage whether it is cheaper to self-host the OpenAI Whisper model, or just use the API client. My theory is that at scale, self-hosting the model turns out to be cheaper.

You can try for yourself like so: 

```bash
curl -X POST -F "file=@/path/to/your/audio/file.mp3" https://athleticshub.cloud/transcribe
```
