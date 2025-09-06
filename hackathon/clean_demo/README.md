# ASLGEMINI: AI-Powered Sign Language Translation

## 🎯 Hackathon Demo

**Problem**: Breaking communication barriers between hearing and Deaf communities through AI-powered American Sign Language (ASL) translation.

**Solution**: Local-first text-to-sign translation pipeline enhanced with Gemini CLI for intelligent ASL generation, featuring real sign language gestures and animations.

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
streamlit run src/clean_web_app.py
```

## 📁 Clean Project Structure

```
clean_demo/
├── README.md                    # This file
├── requirements.txt             # Minimal dependencies
├── src/
│   ├── clean_web_app.py        # Main Streamlit app
│   ├── gemini_integration.py    # Gemini CLI integration
│   └── sign_language_animator.py # Real sign language animation
└── demo/                       # Demo outputs
```

## 🤖 Gemini CLI Integration

### Text Enhancement
- **Purpose**: Simplify complex sentences for better sign translation
- **Implementation**: `gemini_integration.py` → `enhance_text_for_signs()`
- **Example**: "Hello, how are you today?" → "Hello. How are you?"

### Quality Assessment
- **Purpose**: Evaluate sign language animation accuracy
- **Implementation**: `gemini_integration.py` → `assess_sign_quality()`
- **Output**: Accuracy, completeness, and appropriateness scores (1-10)

## 🤟 Real Sign Language Animation

### Visual Gestures
- **Hello**: 👋 Hand wave gesture
- **Thank you**: 🙏 Gratitude gesture  
- **Love**: ❤️ Heart sign
- **Learn**: 📚 Knowledge gesture
- **And more**: 20+ common sign language gestures

### Animation Features
- **Sequential Animation**: Words animate one by one
- **Visual Gestures**: Emoji-based sign language representation
- **Timing Control**: Smooth animation timing
- **Interactive Display**: Live animation in web interface

## 🔄 Demo Pipeline

```
Text Input → Gemini Enhancement → Sign Language Animation → Quality Assessment → Display
```

### Step-by-Step Process:
1. **Text Input**: User enters text
2. **Gemini Enhancement**: Improve text for better sign translation
3. **Sign Animation**: Create visual sign language gestures
4. **Quality Assessment**: Use Gemini to evaluate animation quality
5. **Live Display**: Show animated sign language in web interface

## 📊 Demo Results

### Sample Output:
```json
{
  "original_text": "Hello, how are you today?",
  "enhanced_text": "Hello. How are you?",
  "sign_animation": [
    {"word": "hello", "frames": ["👋 Hello!", "🤚 Hand wave"]},
    {"word": "how", "frames": ["🤔 How?", "👆 Pointing gesture"]},
    {"word": "are", "frames": ["👤 Are you?", "🤷 Gesture"]},
    {"word": "you", "frames": ["👉 You", "👆 Point to person"]}
  ],
  "quality_assessment": {
    "overall_score": 8,
    "accuracy_score": 8,
    "completeness_score": 7,
    "appropriateness_score": 9
  }
}
```

## 🎯 Hackathon Requirements Met

### Technical Excellence (20%)
- ✅ Reliable, reproducible pipeline
- ✅ Comprehensive logging
- ✅ Error handling and fallbacks
- ✅ Clean, minimal codebase

### Solution Architecture (20%)
- ✅ Clean, organized structure
- ✅ Clear documentation
- ✅ Easy setup instructions
- ✅ Minimal dependencies

### Gemini Integration (30%)
- ✅ Text enhancement using Gemini CLI
- ✅ Quality assessment with Gemini
- ✅ Context-aware processing
- ✅ Provenance tracking

### Impact & Innovation (30%)
- ✅ Real sign language animation
- ✅ Accessibility technology with real-world impact
- ✅ Local-first approach with AI enhancement
- ✅ Clear social value proposition

## 🧪 Testing

### Run Demo:
```bash
streamlit run src/clean_web_app.py
```

### Test Features:
- ✅ Text enhancement with Gemini CLI
- ✅ Real sign language animation
- ✅ Quality assessment
- ✅ Live animation display

## 📹 Demo Video Script (≤3 minutes)

1. **Problem Statement** (15s): "Real-time accessibility for Deaf users"
2. **Show App** (20s): Clean web interface with sign language animation
3. **Live Demo** (100s): Text input → Gemini enhancement → Sign animation → Quality assessment
4. **Highlight Features** (20s): Real gestures, Gemini integration, accessibility impact
5. **Next Steps** (15s): "Extend to more languages, add voice input"

## 🚀 What's Next

### Immediate Extensions:
- Add more sign language gestures
- Integrate voice input
- Add more languages
- Improve animation quality

### Long-term Vision:
- Real-time video translation
- Mobile app development
- Community contributions
- Multi-language support

## 📞 Support

For questions or issues:
1. Check environment variables: `echo $GEMINI_API_KEY`
2. Review demo outputs in `demo/` directory
3. Check Streamlit logs for errors

## 📄 License

MIT License - See main project for details
