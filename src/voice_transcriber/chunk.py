from __future__ import annotations

import json
from pathlib import Path


def chunk_transcript(
    transcript_path: Path, output_dir: Path, max_chars: int = 1000
) -> list[Path]:
    """Split a transcript JSON file into smaller text chunks.

    Args:
        transcript_path: Path to the transcription JSON file.
        output_dir: Directory where chunk files will be saved.
        max_chars: Maximum number of characters per chunk.

    Returns:
        A list of paths to the chunk files created.
    """
    if not transcript_path.exists():
        raise FileNotFoundError(f"Transcript file not found: {transcript_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    with open(transcript_path, encoding="utf-8") as f:
        data = json.load(f)
    text = data.get("text", "")

    chunks = [text[i : i + max_chars] for i in range(0, len(text), max_chars)]
    chunk_paths: list[Path] = []
    for idx, chunk in enumerate(chunks, start=1):
        chunk_file = output_dir / f"{transcript_path.stem}_chunk{idx}.txt"
        with open(chunk_file, "w", encoding="utf-8") as f:
            f.write(chunk)
        chunk_paths.append(chunk_file)

    return chunk_paths
