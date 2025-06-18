import json
from pathlib import Path

import pytest

from voice_transcriber.chunk import chunk_transcript


def create_transcript(path: Path, text: str) -> None:
    data = {"text": text}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)


def test_chunk_transcript_splits(tmp_path: Path) -> None:
    transcript = tmp_path / "transcript.json"
    create_transcript(transcript, "a" * 2500)
    output_dir = tmp_path / "chunks"

    paths = chunk_transcript(transcript, output_dir, max_chars=1000)

    assert len(paths) == 3
    for p in paths:
        assert p.exists()
        assert p.read_text(encoding="utf-8")


def test_chunk_transcript_file_missing(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        chunk_transcript(tmp_path / "missing.json", tmp_path)
