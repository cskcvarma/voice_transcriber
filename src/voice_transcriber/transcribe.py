import json
from pathlib import Path
from typing import Any

import whisper


def transcribe_audio(audio_path: Path,
                      output_dir: Path, model_name: str = "base") -> Path:
    """
    Transcribe an audio file using OpenAI Whisper and save the output as JSON.
    
    Args:
        audio_path: Path to the audio file to transcribe
        output_dir: Directory where the output JSON file will be saved
        model_name: Whisper model to use (default: "base")
        
    Returns:
        Path to the saved JSON file
        
    Raises:
        FileNotFoundError: If the audio file doesn't exist
        ValueError: If the model name is invalid
    """
    # Validate input
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load the Whisper model
    try:
        model = whisper.load_model(model_name)
    except Exception as e:
        raise ValueError(f"Failed to load model '{model_name}': {e}") from e
    
    # Transcribe the audio
    result = model.transcribe(str(audio_path))
    
    # Prepare the output data
    output_data: dict[str, Any] = {
        "audio_file": str(audio_path),
        "model": model_name,
        "text": result["text"],
        "language": result.get("language", "unknown"),
        "segments": result.get("segments", []),
        "duration": result.get("duration", 0.0)
    }
    
    # Create output file path
    audio_name = audio_path.stem
    output_file = output_dir / f"{audio_name}.json"
    
    # Save the transcription as JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    return output_file 