# SignBridge Hackathon Deployment Guide

## 🚀 Vercel Deployment

### Prerequisites
- Vercel account
- GitHub repository
- Gemini API key

### Step 1: Prepare Repository
1. Ensure all files are in the `hackathon/` directory
2. Commit and push to GitHub
3. Verify `vercel.json` and `requirements-vercel.txt` are present

### Step 2: Deploy to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Set root directory to `hackathon/`
5. Add environment variable: `GEMINI_API_KEY`

### Step 3: Configure Environment
```bash
# In Vercel dashboard:
GEMINI_API_KEY=your_actual_api_key_here
```

### Step 4: Deploy
- Click "Deploy"
- Wait for build to complete
- Access your app at the provided URL

## 🔧 Local Development

### Quick Start
```bash
# 1. Set environment
export GEMINI_API_KEY=your_key_here

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run demo
./run_demo.sh

# 4. Start web interface
streamlit run src/web_app.py
```

### Development Server
```bash
# Backend (if needed)
cd ../backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000

# Frontend (if needed)
cd ../frontend
npm run dev
```

## 🧪 Testing Before Deployment

### Run Test Suite
```bash
python test_demo.py
```

### Expected Output
```
🧪 SignBridge Hackathon Test Suite
========================================
🔍 Testing Environment Setup...
✅ GEMINI_API_KEY is set
✅ Required dependencies available

📁 Testing File Structure...
✅ src/gemini_integration.py
✅ src/demo_runner.py
✅ src/web_app.py
✅ requirements.txt
✅ .env.example
✅ run_demo.sh
✅ data/sample_phrases.txt

🤖 Testing Gemini CLI Integration...
✅ GeminiEnhancer initialized
✅ Text enhancement working

🎬 Testing Demo Runner...
✅ SignBridgeDemo initialized
✅ Sample demo completed successfully

========================================
📊 Test Results Summary
========================================
✅ PASS Environment Setup
✅ PASS File Structure
✅ PASS Gemini Integration
✅ PASS Demo Runner

🎯 Overall: 4/4 tests passed
🎉 All tests passed! Ready for hackathon demo.
```

## 📊 Demo Checklist

### Before Submission:
- [ ] All tests pass: `python test_demo.py`
- [ ] Demo runs: `./run_demo.sh`
- [ ] Web interface works: `streamlit run src/web_app.py`
- [ ] Vercel deployment successful
- [ ] Environment variables set correctly
- [ ] Documentation complete

### Demo Video Requirements:
- [ ] ≤3 minutes total
- [ ] Show problem statement (15s)
- [ ] Show repo structure (20s)
- [ ] Run live demo (100s)
- [ ] Show safety/logs (20s)
- [ ] Explain next steps (15s)

## 🐛 Troubleshooting

### Common Issues:

#### 1. GEMINI_API_KEY not set
```bash
export GEMINI_API_KEY=your_key_here
echo $GEMINI_API_KEY  # Verify it's set
```

#### 2. Dependencies missing
```bash
pip install -r requirements.txt
```

#### 3. Demo fails
```bash
python test_demo.py  # Check what's failing
```

#### 4. Vercel deployment fails
- Check `vercel.json` syntax
- Verify `requirements-vercel.txt`
- Check environment variables in Vercel dashboard

## 📈 Performance Tips

### For Demo:
- Use short, clear phrases
- Pre-test all functionality
- Have backup demo ready
- Keep dependencies minimal

### For Production:
- Cache Gemini responses
- Optimize model loading
- Add error recovery
- Implement rate limiting

## 🔒 Security Notes

- Never commit API keys to repository
- Use environment variables
- Add `.env` to `.gitignore`
- Use `vercel.json` for deployment secrets
