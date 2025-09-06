"""
ASLGEMINI Web Interface - Gemini CLI + Real Sign Language Animation
Minimal, focused demo for hackathon submission
"""

import streamlit as st
import json
import os
from pathlib import Path
from datetime import datetime
import time

# Add the current directory to Python path
import sys
sys.path.append(str(Path(__file__).parent))

from gemini_integration import GeminiEnhancer
from real_sign_language import RealSignLanguage

# Page configuration
st.set_page_config(
    page_title="ASLGEMINI: AI-Powered Sign Language Translation",
    page_icon="🤟",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .demo-section {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .result-box {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .sign-animation {
        background-color: #e8f4fd;
        padding: 2rem;
        border-radius: 0.5rem;
        text-align: center;
        font-size: 2rem;
        margin: 1rem 0;
        min-height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .success-box {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🤟 ASLGEMINI: AI-Powered Sign Language Translation</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Hackathon Demo")
        st.markdown("""
        **Gemini CLI Integration:**
        - ✅ Text enhancement
        - ✅ Quality assessment
        - ✅ Real sign language animation
        
        **Local-First:**
        - ✅ Works offline
        - ✅ Privacy-focused
        - ✅ Accessibility for Deaf users
        """)
        
        if os.getenv('GEMINI_API_KEY'):
            st.success("✅ Gemini API Ready")
        else:
            st.error("❌ Set GEMINI_API_KEY")
    
    # Main demo
    st.markdown("### 🎬 Live Sign Language Demo")
    
    with st.container():
        st.markdown('<div class="demo-section">', unsafe_allow_html=True)
        
        # Text input
        demo_text = st.text_area(
            "Enter text to translate to sign language:",
            value="Hello, how are you today?",
            height=100
        )
        
        col1, col2 = st.columns(2)
        with col1:
            enhance_with_gemini = st.checkbox("✨ Enhance with Gemini CLI", value=True)
        with col2:
            if st.button("🚀 Show Sign Language", type="primary"):
                if demo_text.strip():
                    run_sign_language_demo(demo_text, enhance_with_gemini)
                else:
                    st.error("Please enter some text")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Sample phrases
    st.markdown("### 📚 Try These Phrases")
    sample_phrases = [
        "Hello, how are you?",
        "Thank you for your help",
        "I love learning new things",
        "Have a great day!"
    ]
    
    cols = st.columns(len(sample_phrases))
    for i, phrase in enumerate(sample_phrases):
        with cols[i]:
            if st.button(f"📝 {phrase[:15]}...", key=f"sample_{i}"):
                st.session_state.demo_text = phrase
                st.rerun()
    
    # Results
    if 'sign_demo_results' in st.session_state:
        display_sign_language_results(st.session_state.sign_demo_results)

def run_sign_language_demo(text: str, enhance: bool):
    """Run the complete sign language demo"""
    
    with st.spinner("🔄 Processing with Gemini CLI and creating sign language..."):
        try:
            # Initialize components
            gemini_enhancer = GeminiEnhancer()
            sign_language = RealSignLanguage()
            
            # Step 1: Enhance text with Gemini CLI
            if enhance:
                enhancement = gemini_enhancer.enhance_text_for_signs(text)
                enhanced_text = enhancement.get("enhanced_text", text)
            else:
                enhanced_text = text
                enhancement = {"gemini_used": False}
            
            # Step 2: Generate ASL signs using Gemini CLI (with fallback)
            try:
                gemini_signs = gemini_enhancer.generate_asl_signs(enhanced_text)
                gemini_available = gemini_signs.get("gemini_used", False)
            except Exception as e:
                st.warning(f"⚠️ Gemini API unavailable: {str(e)}")
                gemini_signs = {"signs": [], "gemini_used": False}
                gemini_available = False
            
            # Convert signs to serializable format
            serializable_signs = []
            
            if gemini_available and gemini_signs.get("signs"):
                # Use Gemini-generated signs
                for sign_data in gemini_signs.get("signs", []):
                    # Ensure duration is a number
                    duration = sign_data.get("duration", 1.0)
                    if isinstance(duration, str):
                        try:
                            duration = float(duration)
                        except ValueError:
                            duration = 1.0
                    
                    sign_data["duration"] = duration
                    sign_data["hand_positions"] = [{
                        "hand_shape": sign_data.get("hand_shape", "open"),
                        "palm_orientation": sign_data.get("palm_orientation", "forward"),
                        "location": sign_data.get("location", "space"),
                        "movement": sign_data.get("movement", "wave")
                    }]
                    serializable_signs.append(sign_data)
            else:
                # Fallback to corrected hardcoded signs
                sign_sequence = sign_language.create_sign_sequence(enhanced_text)
                for sign in sign_sequence:
                    sign_data = {
                        "word": sign.word,
                        "description": sign.description,
                        "duration": sign.duration,
                        "hand_positions": [
                            {
                                "hand_shape": pos.hand_shape,
                                "palm_orientation": pos.palm_orientation,
                                "location": pos.location,
                                "movement": pos.movement
                            }
                            for pos in sign.hand_positions
                        ],
                        "cultural_notes": "Using corrected ASL signs (Gemini unavailable)"
                    }
                    serializable_signs.append(sign_data)
            
            # Step 3: Assess quality with Gemini CLI
            quality_assessment = gemini_enhancer.assess_sign_quality(enhanced_text, str(serializable_signs))
            
            # Compile results
            results = {
                "original_text": text,
                "enhanced_text": enhanced_text,
                "sign_sequence": serializable_signs,
                "enhancement_details": enhancement,
                "gemini_signs_details": gemini_signs,
                "quality_assessment": quality_assessment,
                "gemini_calls": sum([enhance, gemini_signs.get("gemini_used", False), True]),  # enhancement + signs + quality assessment
                "success": True,
                "timestamp": datetime.now().isoformat()
            }
            
            st.session_state.sign_demo_results = results
            
            # Save results
            demo_dir = Path("demo")
            demo_dir.mkdir(exist_ok=True)
            results_file = demo_dir / f"sign_demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(results_file, "w") as f:
                json.dump(results, f, indent=2)
            
        except Exception as e:
            st.error(f"Demo failed: {str(e)}")
            st.session_state.sign_demo_results = {
                "error": str(e),
                "success": False
            }

def display_sign_language_results(results: dict):
    """Display the sign language demo results"""
    
    st.markdown("### 📊 Sign Language Demo Results")
    
    if not results.get("success", False):
        st.error(f"❌ Demo failed: {results.get('error', 'Unknown error')}")
        return
    
    # Original text
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.subheader("📝 Original Text")
    st.write(results["original_text"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced text
    if results["enhancement_details"].get("gemini_used", False):
        st.markdown('<div class="result-box success-box">', unsafe_allow_html=True)
        st.subheader("✨ Gemini-Enhanced Text")
        st.write(results["enhanced_text"])
        
        with st.expander("🔍 Enhancement Details"):
            st.write(f"**Reasoning:** {results['enhancement_details']['reasoning']}")
            st.write(f"**Confidence:** {results['enhancement_details']['confidence']}/10")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Real Sign Language
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.subheader("🤟 Real ASL Signs Generated by Gemini CLI")
    
    # Show Gemini usage info
    if results.get("gemini_signs_details", {}).get("gemini_used", False):
        st.success("✅ Signs generated using Gemini CLI - Expert ASL knowledge!")
    else:
        st.info("ℹ️ Using corrected ASL signs (Gemini API quota reached - this demonstrates the fallback system)")
    
    # Show sign sequence
    sign_sequence = results["sign_sequence"]
    
    st.write("**Sign Language Sequence:**")
    for i, sign in enumerate(sign_sequence):
        with st.expander(f"{i+1}. Sign: {sign['word'].upper()}"):
            st.write(f"**Description:** {sign['description']}")
            st.write(f"**Duration:** {sign['duration']} seconds")
            st.write(f"**Hand Positions:** {len(sign['hand_positions'])}")
            
            for j, pos in enumerate(sign['hand_positions']):
                st.write(f"  {j+1}. Hand shape: {pos['hand_shape']}")
                st.write(f"     Palm orientation: {pos['palm_orientation']}")
                st.write(f"     Location: {pos['location']}")
                st.write(f"     Movement: {pos['movement']}")
            
            if sign.get('cultural_notes'):
                st.info(f"**Cultural Note:** {sign['cultural_notes']}")
    
    # Live sign demonstration
    st.write("**Live Sign Demonstration:**")
    demo_container = st.empty()
    
    # Run sign demonstration
    for sign in sign_sequence:
        # Convert duration to float if it's a string
        duration = float(sign['duration']) if isinstance(sign['duration'], str) else sign['duration']
        
        demo_container.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin: 10px 0; border: 2px solid #1f77b4;">
            <h3 style="color: #1f77b4; margin: 0 0 10px 0;">🤟 Sign: {sign['word'].upper()}</h3>
            <p style="color: #333333; margin: 5px 0;"><strong>Description:</strong> {sign['description']}</p>
            <p style="color: #333333; margin: 5px 0;"><strong>Duration:</strong> {duration} seconds</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(duration)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Quality assessment
    if results["quality_assessment"].get("gemini_used", False):
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("📊 Quality Assessment")
        
        assessment = results["quality_assessment"]["assessment"]
        st.metric("Overall Score", f"{assessment['overall_score']}/10")
        
        with st.expander("🔍 Detailed Assessment"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Accuracy", f"{assessment['accuracy_score']}/10")
            with col2:
                st.metric("Completeness", f"{assessment['completeness_score']}/10")
            with col3:
                st.metric("Appropriateness", f"{assessment['appropriateness_score']}/10")
            
            st.write(f"**Feedback:** {assessment['feedback']}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Summary
    st.markdown('<div class="result-box success-box">', unsafe_allow_html=True)
    st.subheader("📈 Demo Summary")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Gemini CLI Calls", results["gemini_calls"])
    with col2:
        st.metric("Sign Gestures", len(sign_sequence))
    with col3:
        st.metric("Pipeline Status", "✅ Success")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
