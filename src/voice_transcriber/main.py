from __future__ import annotations

from pathlib import Path

from voice_transcriber.chunk import chunk_transcript
from voice_transcriber.transcribe import transcribe_audio


def main() -> None:
    """Transcribe an audio file and chunk the resulting transcript."""
    audio_file = Path("audio/interview.m4a")
    output_dir = Path("output")

    transcript_path = transcribe_audio(audio_file, output_dir)
    chunk_transcript(transcript_path, output_dir)


