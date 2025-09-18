# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python sound notification project that plays a WAV file (`nice.wav`) when the main script is executed. The project uses Python 3.12 and is configured with `pyproject.toml`.

## Key Files

- `playnotice.py`: Main Python script that plays the `nice.wav` sound file
- `nice.wav`: Audio file that gets played when the script runs
- `pyproject.toml`: Python project configuration file

## Running the Application

```bash
python playnotice.py
```

## Development Tools

The project has the following development tools available:
- `pytest`: For running tests (though no tests are currently present)
- `ruff`: For Python linting and formatting

### Linting

```bash
ruff check .
ruff format .
```

## Architecture Notes

The `playnotice.py` script uses platform-specific audio playback:
- Windows: Uses the built-in `winsound` module
- macOS: Uses the `afplay` command
- Linux: Attempts to use `pygame`, falls back to `aplay` or `play` commands

The script automatically detects the WAV file location relative to the script's directory using `pathlib.Path`.