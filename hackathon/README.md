# ASLGEMINI: AI-Powered Sign Language Translation

## 🎯 Hackathon Submission

**Problem**: Breaking communication barriers between hearing and Deaf communities through AI-powered American Sign Language (ASL) translation.

**Solution**: Local-first text-to-sign translation pipeline enhanced with Gemini CLI for intelligent ASL generation and quality assessment.

## 🚀 Quick Start

### 1. Set Environment Variables
```bash
export GEMINI_API_KEY=your_gemini_api_key_here
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Demo
```bash
# File processing demo
python process_files.py

# Web interface
streamlit run src/clean_web_app.py --server.port 8502
```

## 📁 Project Structure

```
hackathon/
├── README.md                    # This file
├── HACKATHON_README.md         # Hackathon-specific documentation
├── requirements.txt             # Python dependencies
├── .env.example                # Environment variables template
├── vercel.json                 # Vercel deployment config
├── clean_demo/                 # Main hackathon entry
│   ├── src/
│   │   ├── clean_web_app.py    # Streamlit web interface
│   │   ├── gemini_integration.py # Gemini CLI integration
│   │   ├── real_sign_language.py # ASL sign system
│   │   └── file_processor.py   # File processing system
│   ├── process_files.py        # File processing script
│   └── requirements.txt        # Dependencies
├── ASL_input/                  # Input text files
└── ASL_output/                 # Generated ASL results
```

## 🤖 Gemini CLI Integration

### Text Enhancement
- **Purpose**: Simplify complex sentences for better sign translation
- **Implementation**: `gemini_integration.py` → `enhance_text_for_signs()`
- **Example**: "The quick brown fox jumps over the lazy dog" → "Quick brown fox jumps over lazy dog"

### Quality Assessment
- **Purpose**: Evaluate sign translation accuracy and completeness
- **Implementation**: `gemini_integration.py` → `assess_sign_quality()`
- **Output**: Accuracy, completeness, and appropriateness scores (1-10)

### Context Understanding
- **Purpose**: Add domain-specific context for better translation
- **Implementation**: `gemini_integration.py` → `add_context_for_signs()`
- **Use Cases**: Medical terms, technical concepts, emotional context

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
  "original_text": "Hello, how are you today?",
  "enhanced_text": "Hello! How are you today?",
  "signwriting_output": "M123x456S12345",
  "enhancement_details": {
    "reasoning": "Added punctuation for clarity",
    "confidence": 8
  },
  "quality_assessment": {
    "overall_score": 9,
    "accuracy_score": 9,
    "completeness_score": 8,
    "appropriateness_score": 9
  }
}
```

## 🌐 Vercel Deployment

### Deploy to Vercel:
1. Connect your GitHub repo to Vercel
2. Set `GEMINI_API_KEY` in Vercel environment variables
3. Deploy from the `hackathon/` directory

### Vercel Configuration:
- **Framework**: Python/Streamlit
- **Build Command**: `pip install -r requirements-vercel.txt`
- **Output Directory**: `src/`
- **Environment Variables**: `GEMINI_API_KEY`

## 🧪 Testing

### Run Test Suite:
```bash
python test_demo.py
```

### Test Coverage:
- ✅ Environment setup
- ✅ File structure
- ✅ Gemini CLI integration
- ✅ Demo runner functionality

## 📹 Demo Video Script (≤3 minutes)

1. **Problem Statement** (15s): "Real-time accessibility for Deaf users"
2. **Show Repo** (20s): README + key files + Gemini CLI integration points
3. **Live Demo** (100s): Text input → Gemini enhancement → SignWriting → Quality assessment
4. **Safety/Logs** (20s): Show confirmation steps and saved outputs
5. **Next Steps** (15s): "Extend to more languages, add GitHub Actions"

## 🎯 Hackathon Requirements Met

### Technical Excellence (20%)
- ✅ Reliable, reproducible pipeline
- ✅ Comprehensive logging
- ✅ Error handling and fallbacks
- ✅ Test suite verification

### Solution Architecture (20%)
- ✅ Clean, organized codebase
- ✅ Clear documentation
- ✅ Easy setup instructions
- ✅ Proper environment management

### Gemini Integration (30%)
- ✅ Text enhancement using Gemini CLI
- ✅ Quality assessment with Gemini
- ✅ Context-aware processing
- ✅ Chain-of-thought reasoning
- ✅ Provenance tracking

### Impact & Innovation (30%)
- ✅ Accessibility technology with real-world impact
- ✅ Local-first approach with AI enhancement
- ✅ Clear social value proposition
- ✅ Potential for broader adoption

## 🔧 Local vs Cloud Processing

### Local Processing:
- **Streamlit**: Web interface for text input and sign display
- **SignWriting Model**: Text-to-sign translation
- **Core Pipeline**: Works entirely offline

### Cloud Processing (Gemini CLI):
- **Text Enhancement**: Improve text for better signs
- **Quality Assessment**: Evaluate translation accuracy
- **Context Understanding**: Add domain-specific context

## 🚀 What's Next

### Immediate Extensions:
- Add more languages beyond English
- Integrate GitHub Actions for automated testing
- Add slash commands for advanced text processing
- Extend to real-time video translation

### Long-term Vision:
- Multi-language support
- Real-time video translation
- Mobile app development
- Community contributions

## 📞 Support

For questions or issues:
1. Check the test suite: `python test_demo.py`
2. Review logs in `demo/demo_log.jsonl`
3. Check environment variables: `echo $GEMINI_API_KEY`

## 📄 License

MIT License - See main project for details
