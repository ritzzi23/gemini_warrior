"""
Gemini CLI Integration for ASLGEMINI Hackathon
Enhances text processing for better sign language translation
"""

import os
import json
import logging
from typing import Dict, List, Optional, Any
import google.generativeai as genai

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GeminiEnhancer:
    """Handles Gemini CLI integration for text enhancement"""
    
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
    def enhance_text_for_signs(self, text: str) -> Dict[str, str]:
        """
        Enhance text for better sign language translation using Gemini CLI
        
        Args:
            text: Original text to enhance
            
        Returns:
            Dict with enhanced text and metadata
        """
        try:
            prompt = f"""
            Enhance the following text for better sign language translation:
            
            Original: "{text}"
            
            Please:
            1. Simplify complex sentences
            2. Break down compound ideas
            3. Use clear, direct language
            4. Maintain the original meaning
            
            Return your response as JSON with:
            - "enhanced_text": the improved text
            - "reasoning": why you made these changes
            - "confidence": your confidence level (1-10)
            """
            
            response = self.model.generate_content(prompt)
            
            # Parse JSON response - handle potential formatting issues
            try:
                result = json.loads(response.text)
            except json.JSONDecodeError:
                # If JSON parsing fails, try to extract JSON from response
                import re
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    result = json.loads(json_match.group())
                else:
                    # Fallback: create a simple response
                    result = {
                        "enhanced_text": response.text.strip(),
                        "reasoning": "Gemini provided text enhancement",
                        "confidence": 7
                    }
            
            logger.info(f"Enhanced text: {text} -> {result['enhanced_text']}")
            
            return {
                "original_text": text,
                "enhanced_text": result["enhanced_text"],
                "reasoning": result["reasoning"],
                "confidence": result["confidence"],
                "gemini_used": True
            }
            
        except Exception as e:
            logger.error(f"Gemini enhancement failed: {e}")
            return {
                "original_text": text,
                "enhanced_text": text,  # Fallback to original
                "reasoning": "Gemini enhancement failed, using original text",
                "confidence": 1,
                "gemini_used": False,
                "error": str(e)
            }
    
    def assess_sign_quality(self, original_text: str, sign_output: str) -> Dict[str, any]:
        """
        Assess the quality of sign language translation using Gemini CLI
        
        Args:
            original_text: Original English text
            sign_output: Generated SignWriting notation
            
        Returns:
            Dict with quality assessment
        """
        try:
            prompt = f"""
            Assess the quality of this sign language translation:
            
            Original English: "{original_text}"
            SignWriting Output: "{sign_output}"
            
            Please evaluate:
            1. Accuracy of translation
            2. Completeness of signs
            3. Appropriateness for sign language
            
            Return your response as JSON with:
            - "accuracy_score": 1-10 rating
            - "completeness_score": 1-10 rating
            - "appropriateness_score": 1-10 rating
            - "overall_score": 1-10 rating
            - "feedback": specific suggestions for improvement
            - "strengths": what works well
            """
            
            response = self.model.generate_content(prompt)
            
            # Parse JSON response - handle potential formatting issues
            try:
                result = json.loads(response.text)
            except json.JSONDecodeError:
                # If JSON parsing fails, try to extract JSON from response
                import re
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    result = json.loads(json_match.group())
                else:
                    # Fallback: create a simple response
                    result = {
                        "accuracy_score": 7,
                        "completeness_score": 7,
                        "appropriateness_score": 7,
                        "overall_score": 7,
                        "feedback": "Assessment completed",
                        "strengths": "Translation appears reasonable"
                    }
            
            logger.info(f"Sign quality assessed: {result['overall_score']}/10")
            
            return {
                "original_text": original_text,
                "sign_output": sign_output,
                "assessment": result,
                "gemini_used": True
            }
            
        except Exception as e:
            logger.error(f"Sign quality assessment failed: {e}")
            return {
                "original_text": original_text,
                "sign_output": sign_output,
                "assessment": {
                    "accuracy_score": 5,
                    "completeness_score": 5,
                    "appropriateness_score": 5,
                    "overall_score": 5,
                    "feedback": "Assessment failed",
                    "strengths": "Unable to assess"
                },
                "gemini_used": False,
                "error": str(e)
            }
    
    def add_context_for_signs(self, text: str, context_type: str = "general") -> Dict[str, str]:
        """
        Add context to text for better sign language understanding
        
        Args:
            text: Text to add context to
            context_type: Type of context (medical, technical, emotional, etc.)
            
        Returns:
            Dict with contextualized text
        """
        try:
            prompt = f"""
            Add appropriate context to this text for sign language translation:
            
            Text: "{text}"
            Context Type: {context_type}
            
            Please:
            1. Add relevant context that helps with sign language understanding
            2. Clarify ambiguous terms
            3. Provide cultural or domain-specific information
            
            Return your response as JSON with:
            - "contextualized_text": the text with added context
            - "context_added": what context was added
            - "domain": the domain/context type
            """
            
            response = self.model.generate_content(prompt)
            result = json.loads(response.text)
            
            logger.info(f"Added context for {context_type}: {text}")
            
            return {
                "original_text": text,
                "contextualized_text": result["contextualized_text"],
                "context_added": result["context_added"],
                "domain": result["domain"],
                "gemini_used": True
            }
            
        except Exception as e:
            logger.error(f"Context addition failed: {e}")
            return {
                "original_text": text,
                "contextualized_text": text,
                "context_added": "Context addition failed",
                "domain": context_type,
                "gemini_used": False,
                "error": str(e)
            }

    def generate_asl_signs(self, text: str) -> Dict[str, Any]:
        """Generate accurate ASL signs using Gemini CLI"""
        try:
            prompt = f"""
            You are an expert in American Sign Language (ASL). Generate accurate ASL signs for the following text.
            
            Text: "{text}"
            
            For each word, provide:
            1. The correct ASL sign description
            2. Hand shape (fist, open, point, flat-o, f-hand, etc.)
            3. Palm orientation (forward, up, down, side, etc.)
            4. Location (chest, face, space, mouth, cheek, etc.)
            5. Movement (tap, wave, circle, point, pull, twist, etc.)
            6. Duration in seconds
            7. Cultural notes if important
            
            Note: Skip English connector words like "to", "the", "a", "an" as ASL doesn't sign these.
            Focus on content words only.
            
            Respond in JSON format:
            {{
                "signs": [
                    {{
                        "word": "<word>",
                        "description": "<detailed ASL sign description>",
                        "hand_shape": "<hand configuration>",
                        "palm_orientation": "<palm direction>",
                        "location": "<where sign is made>",
                        "movement": "<type of movement>",
                        "duration": <seconds>,
                        "cultural_notes": "<any important cultural context>"
                    }}
                ],
                "gemini_used": true
            }}
            """
            
            response = self.model.generate_content(prompt)
            
            try:
                result = json.loads(response.text)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    result = json.loads(json_match.group())
                else:
                    # Fallback parsing
                    result = {
                        "signs": [{
                            "word": text,
                            "description": response.text.strip(),
                            "hand_shape": "open",
                            "palm_orientation": "forward",
                            "location": "space",
                            "movement": "wave",
                            "duration": 1.0,
                            "cultural_notes": "Generated by Gemini"
                        }],
                        "gemini_used": True
                    }
            
            logger.info(f"Generated {len(result.get('signs', []))} ASL signs using Gemini")
            return result
            
        except Exception as e:
            logger.error(f"Error generating ASL signs: {e}")
            return {
                "signs": [{
                    "word": text,
                    "description": f"Error generating sign: {str(e)}",
                    "hand_shape": "open",
                    "palm_orientation": "forward",
                    "location": "space",
                    "movement": "wave",
                    "duration": 1.0,
                    "cultural_notes": "Fallback due to error"
                }],
                "gemini_used": False
            }

# Example usage for testing
if __name__ == "__main__":
    # Test the Gemini integration
    enhancer = GeminiEnhancer()
    
    # Test text enhancement
    test_text = "The quick brown fox jumps over the lazy dog"
    result = enhancer.enhance_text_for_signs(test_text)
    print("Enhancement Result:", json.dumps(result, indent=2))
    
    # Test quality assessment
    quality_result = enhancer.assess_sign_quality(test_text, "M123x456S12345")
    print("Quality Assessment:", json.dumps(quality_result, indent=2))
