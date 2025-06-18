# `transcribe` Module

`transcribe_audio(audio_path: Path, output_dir: Path, model_name: str = "base") -> Path`

Transcribes an audio file using OpenAI Whisper and saves the result as a JSON file. The returned `Path` points to the generated JSON transcript.

Example:

```python
from pathlib import Path
from voice_transcriber.transcribe import transcribe_audio

transcript = transcribe_audio(Path("audio.wav"), Path("out"))
print(transcript.read_text())
```
