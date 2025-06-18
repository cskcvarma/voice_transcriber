# Voice Transcriber

A small utility that uses [OpenAI Whisper](https://github.com/openai/whisper) to transcribe audio files and split the transcript into manageable chunks.

## Installation

Install with [uv](https://github.com/astral-sh/uv) to ensure all development dependencies are available:

```bash
uv pip install -e .[dev]
```

## Usage

The package exposes a console script:

```bash
uv run voice_transcriber
```

This will transcribe `audio/interview.m4a` and write chunks to the `output` directory.

See the docs in `docs/voice_transcriber/` for details about each module.

## Development

Run formatting, linting, type checking and tests using [nox](https://nox.thea.codes/):

```bash
uv run nox
```
