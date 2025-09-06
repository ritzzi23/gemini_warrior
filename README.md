# ASLGEMINI - AI-Powered Sign Language Translation

A **fast, local-first prototype** for the Gemini CLI Buildathon that demonstrates AI-powered American Sign Language (ASL) translation using Gemini CLI integration.

## 🎯 Problem Statement

Breaking communication barriers between hearing and Deaf communities through AI-powered sign language translation, making communication more accessible and inclusive.

## 🚀 Quick Start

1. Set your Gemini API key: `export GEMINI_API_KEY=your_key_here`
2. Navigate to hackathon demo: `cd hackathon/clean_demo`
3. Install dependencies: `pip install -r requirements.txt`
4. Run web interface: `streamlit run src/clean_web_app.py --server.port 8502`
5. Process files: `python process_files.py`

## 🤖 Gemini CLI Integration

- **Text Enhancement**: Simplifies complex sentences for better sign translation
- **ASL Sign Generation**: Generates accurate American Sign Language signs with cultural context
- **Quality Assessment**: Evaluates accuracy and appropriateness of generated signs
- **Cultural Context**: Adds important cultural and regional variations

## 📁 Project Structure

```
ASLGEMINI/
├── README.md                    # This file
├── HACKATHON_README.md         # Hackathon-specific documentation
├── hackathon/                   # Main hackathon entry
│   ├── clean_demo/              # Clean demo implementation
│   │   ├── src/
│   │   │   ├── clean_web_app.py    # Streamlit web interface
│   │   │   ├── gemini_integration.py # Gemini CLI integration
│   │   │   ├── real_sign_language.py # ASL sign system
│   │   │   └── file_processor.py   # File processing system
│   │   ├── process_files.py        # File processing script
│   │   └── requirements.txt        # Dependencies
│   └── README.md                   # Hackathon documentation
├── ASL_input/                   # Input text files
└── ASL_output/                  # Generated ASL results
```

## 🔄 Demo Pipeline

```
Text Input → Gemini Enhancement → ASL Sign Generation → Quality Assessment → Display
```

### Step-by-Step Process:
1. **Text Input**: User enters text to translate
2. **Gemini Enhancement**: Improve text for better sign translation
3. **ASL Sign Generation**: Generate accurate American Sign Language signs
4. **Quality Assessment**: Use Gemini to evaluate translation quality
5. **Display**: Show results with live sign demonstrations

## 📊 Demo Results

### Sample Output:
```json
{
  "original_text": "I am feeling hungry today.",
  "enhanced_text": "I am hungry.",
  "signs": [
    {
      "word": "I",
      "description": "Point to oneself with index finger",
      "hand_shape": "Index finger",
      "location": "Chest",
      "movement": "Tap",
      "cultural_notes": "Common and straightforward sign"
    },
    {
      "word": "hungry",
      "description": "Bring cupped hand to mouth, mimicking eating",
      "hand_shape": "Open hand, slightly cupped",
      "location": "Mouth",
      "movement": "Bring hand to mouth"
    }
  ],
  "quality_score": 9.0,
  "gemini_calls": 3
}
```

## 🎯 Hackathon Alignment

- ✅ **Gemini Integration**: Deep CLI integration with multiple AI functions
- ✅ **Local-First**: Works entirely on-device with local processing
- ✅ **Reproducible**: Clear setup and demo instructions
- ✅ **Impact**: Real accessibility solution for Deaf community
- ✅ **Technical Excellence**: Clean architecture with error handling

## 🔧 Local vs Cloud Processing

### Local Processing:
- **Streamlit**: Web interface for text input and sign display
- **File Processing**: Batch processing of text files
- **Core Pipeline**: Works entirely offline

### Cloud Processing (Gemini CLI):
- **Text Enhancement**: Improve text for better signs
- **ASL Generation**: Generate accurate sign language
- **Quality Assessment**: Evaluate translation accuracy
- **Cultural Context**: Add cultural and regional variations

## 🚀 Next Steps

- [ ] Deploy to Vercel for public access
- [ ] Add more sign language support (BSL, LSF, etc.)
- [ ] Integrate with mobile apps
- [ ] Add voice input support
- [ ] Create educational modules

## 📝 Notes

This is a **hackathon prototype** focused on demonstrating Gemini CLI capabilities for accessibility applications. The system prioritizes speed, reproducibility, and clear demonstration of AI integration over production-ready features.

## 🏆 Judging Criteria Alignment

- **Gemini Integration (30%)**: Multiple AI functions, expert ASL knowledge
- **Technical Excellence (20%)**: Clean code, error handling, logging
- **Impact (30%)**: Real accessibility solution, local processing
- **Architecture (20%)**: Clear structure, documentation, demo-ready

## 🔗 Resources

- [Gemini CLI Documentation](https://ai.google.dev/gemini-api/docs)
- [American Sign Language Resources](https://www.nad.org/)
- [Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

**Built for the Gemini CLI Buildathon** 🏆
