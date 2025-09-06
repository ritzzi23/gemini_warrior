# ASLGEMINI: AI-Powered Sign Language Translation

## Problem
Breaking communication barriers between hearing and Deaf communities through AI-powered American Sign Language (ASL) translation with Gemini CLI integration.

## How to Run
1. Set `GEMINI_API_KEY` environment variable
2. Run `python process_files.py` (reads ASL_input/, writes ASL_output/)
3. Open http://localhost:8502 for web interface

## Where Gemini CLI is Called
- `src/gemini_integration.py` → calls Gemini CLI to enhance text for better sign translation
- `src/gemini_integration.py` → uses Gemini CLI to generate accurate ASL signs
- `src/gemini_integration.py` → uses Gemini CLI to evaluate sign translation accuracy

## What's Local
- `ASL_input/` (input text files)
- `ASL_output/` (output ASL signs and reports)
- File processing pipeline (runs locally)
- Web interface (runs locally)

## What's Hard/Interesting
- **AI-Powered ASL**: Text → AI Enhancement → Accurate Sign Language
- **Local-First**: Core functionality works offline, Gemini CLI enhances when available
- **Accessibility Impact**: Real-world utility for Deaf community
- **Cultural Context**: Includes regional variations and cultural notes

## What's Next
- Add more sign languages beyond ASL (BSL, LSF, etc.)
- Integrate GitHub Actions for automated testing
- Add slash commands for advanced text processing
- Extend to real-time video translation

## Gemini CLI Integration Features
- **Text Enhancement**: Simplify complex sentences for better sign translation
- **ASL Sign Generation**: Generate accurate American Sign Language signs
- **Quality Assessment**: Evaluate sign translation accuracy
- **Cultural Context**: Add regional variations and cultural notes

## Demo Video Script (≤3 minutes)
1. **Problem**: "Breaking communication barriers for Deaf users" (15s)
2. **Show Repo**: README + key files + Gemini CLI integration points (20s)
3. **Live Demo**: Text files → Gemini CLI → ASL signs → Save output (100s)
4. **Safety/Logs**: Show confirmation steps and saved outputs (20s)
5. **Next Steps**: "Extend to more languages, add GitHub Actions" (15s)