# Voice Transcriber

This project transcribes audio files into text using OpenAI Whisper, splits long transcripts into manageable text chunks and provides a simple CLI entry point.  It is structured as a small library so the individual pieces can be reused in other projects.

Available modules:

- `transcribe`: utilities for transcribing audio files to JSON.
- `chunk`: tools for splitting a transcript into smaller pieces.
- `main`: command line entry that ties everything together.

See the individual module pages for usage information.
