#!/bin/bash

# SignBridge Clean Demo Runner
echo "🤟 Starting SignBridge Clean Demo"
echo "=================================="

# Check if GEMINI_API_KEY is set
if [ -z "$GEMINI_API_KEY" ]; then
    echo "❌ Error: GEMINI_API_KEY environment variable is required"
    echo "   Please set it with: export GEMINI_API_KEY=your_key_here"
    exit 1
fi

echo "✅ GEMINI_API_KEY is set"

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🚀 Starting web interface..."
echo "   Open: http://localhost:8502"
echo ""

# Start Streamlit
streamlit run src/clean_web_app.py --server.port 8502
