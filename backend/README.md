# SignBridge Backend

## Overview

This backend provides the core API services for the SignBridge application, including:

- Offline speech-to-text transcription using the Python Whisper library
- Optional online text simplification via Groq API
- Text-to-SignWriting translation using the signwriting-translation package with PyTorch

## Features / Endpoints

### POST /transcribe

- Accepts: WAV audio file (multipart/form-data)
- Returns: JSON with transcribed text
- Uses: Python Whisper library for offline transcription

### POST /simplify_text

- Accepts: JSON with text string
- Returns: JSON with simplified text string
- Uses: Groq API for optional online text simplification

### POST /translate_signwriting

- Accepts: JSON with text string
- Returns: JSON with SignWriting notation string
- Uses: signwriting-translation PyTorch model for text-to-sign translation

### POST /generate_pose

- Accepts: JSON with text and language parameters
- Returns: JSON with base64-encoded pose data
- Uses: External pose generation API

## Environment Configuration

The backend uses environment variables for configuration. Copy `env.example` to `.env` and configure the following:

### Required Environment Variables

```bash
# Server Configuration
HOST=127.0.0.1
PORT=8000
DEBUG=true

# API Keys and External Services
GROQ_API_KEY=your_groq_api_key_here
GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions

# Pose Generation API
POSE_API_URL=https://us-central1-sign-mt.cloudfunctions.net/spoken_text_to_signed_pose

# Whisper Model Configuration
WHISPER_MODEL=base
WHISPER_DEVICE=cpu

# CORS Configuration
CORS_ORIGINS=["*"]
CORS_ALLOW_CREDENTIALS=true
CORS_ALLOW_METHODS=["*"]
CORS_ALLOW_HEADERS=["*"]

# Logging
LOG_LEVEL=DEBUG
```

### Setup Environment

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` and add your actual values:
   - Get a Groq API key from [https://api.groq.com](https://api.groq.com)
   - Configure other settings as needed

## Setup

### System Dependencies

- **ffmpeg**: Required for audio file conversion in the /transcribe endpoint. Install it using your system package manager:
  - macOS: `brew install ffmpeg`
  - Ubuntu/Debian: `sudo apt-get install ffmpeg`
  - Windows: [Download from ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

- **Python Whisper Library**: Used for speech-to-text transcription. The backend will automatically download the required model files on first use.

### Python 3.11 Environment

- Make sure you are in the backend folder

```bash
# Install Python 3.11 if not installed
brew install python@3.11

# Run setup script to create and activate Python 3.11 virtual environment and install dependencies
bash ./setup_py311_env.sh

# Activate the Python 3.11 environment
source py311_venv/bin/activate
```

## Running the Backend

When the desired environment is activated, run:

```bash
# Using the run script
python run_backend.py

# Or directly with uvicorn
uvicorn main:app --reload
```

The backend will be available at the configured HOST:PORT (default: `http://127.0.0.1:8000`).

## Configuration

The backend uses a centralized configuration system in `config.py` that loads all settings from environment variables. This makes it easy to:

- Deploy to different environments (development, staging, production)
- Configure API keys and external service URLs
- Adjust server settings and CORS policies
- Control logging levels

## Notes

- The Python Whisper library will download model files as needed on first use.
- The Groq API key and URL should be configured in the `.env` file.
- The text-to-SignWriting translation requires the Python 3.11 environment due to PyTorch compatibility.

## Testing

Test scripts are located in the `tests/` directory:

- `test_transcribe.py`
- `test_simplify_text.py`
- `test_translate_signwriting.py`

Run tests using the appropriate Python environment. Test scripts will use the `BACKEND_URL` environment variable or default to `http://127.0.0.1:8000`.

## License

This project is licensed under the MIT License.
