# `chunk` Module

`chunk_transcript(transcript_path: Path, output_dir: Path, max_chars: int = 1000) -> list[Path]`

Splits a transcript JSON file into a series of text files each containing at most `max_chars` characters. Returns a list of paths to the created chunk files.

Example:

```python
from pathlib import Path
from voice_transcriber.chunk import chunk_transcript

chunks = chunk_transcript(Path("transcript.json"), Path("out"))
for chunk in chunks:
    print(chunk.read_text())
```
