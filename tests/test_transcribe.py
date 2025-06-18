import json
import types
import sys
from pathlib import Path

import pytest

# Create a dummy whisper module before importing transcribe
whisper_mock = types.ModuleType("whisper")

class DummyModel:
    def transcribe(self, path: str):
        return {"text": "hello", "language": "en", "segments": [], "duration": 1.0}

def load_model(name: str) -> DummyModel:
    return DummyModel()

whisper_mock.load_model = load_model
sys.modules["whisper"] = whisper_mock

from voice_transcriber.transcribe import transcribe_audio


def test_transcribe_audio(tmp_path: Path) -> None:
    audio = tmp_path / "audio.wav"
    audio.write_text("dummy")
    output_dir = tmp_path / "out"

    result_path = transcribe_audio(audio, output_dir)
    assert result_path.exists()
    with open(result_path, encoding="utf-8") as f:
        data = json.load(f)
    assert data["text"] == "hello"


def test_transcribe_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        transcribe_audio(tmp_path / "missing.wav", tmp_path)
