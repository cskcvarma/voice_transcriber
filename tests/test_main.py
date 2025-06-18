import importlib
import sys
import types
from pathlib import Path


def test_main_invokes_transcribe_and_chunk(monkeypatch, tmp_path):
    whisper_mock = types.ModuleType("whisper")

    class DummyModel:
        def transcribe(self, path: str):
            return {"text": "dummy"}

    whisper_mock.load_model = lambda name: DummyModel()
    monkeypatch.setitem(sys.modules, "whisper", whisper_mock)

    main_module = importlib.import_module("voice_transcriber.main")
    importlib.reload(main_module)

    calls = {}

    def fake_transcribe(audio_path: Path, output_dir: Path):
        calls["transcribe"] = (audio_path, output_dir)
        return tmp_path / "transcript.json"

    def fake_chunk(transcript_path: Path, output_dir: Path, max_chars: int = 1000):
        calls["chunk"] = (transcript_path, output_dir, max_chars)
        return [output_dir / "chunk1.txt"]

    monkeypatch.setattr(main_module, "transcribe_audio", fake_transcribe)
    monkeypatch.setattr(main_module, "chunk_transcript", fake_chunk)

    main_module.main()

    assert calls["transcribe"] == (Path("audio/interview.m4a"), Path("output"))
    assert calls["chunk"] == (
        tmp_path / "transcript.json",
        Path("output"),
        1000,
    )
