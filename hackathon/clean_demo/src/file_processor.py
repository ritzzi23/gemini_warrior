"""
ASLGEMINI File Processing System
Demonstrates local file processing with Gemini CLI integration
"""

import os
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
from gemini_integration import GeminiEnhancer
from real_sign_language import RealSignLanguage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ASLGEMINIFileProcessor:
    """Process text files and generate ASL signs using Gemini CLI"""
    
    def __init__(self):
        self.gemini_enhancer = GeminiEnhancer()
        self.sign_language = RealSignLanguage()
        
        # Define input/output directories
        self.input_dir = Path("../../ASL_input")
        self.output_dir = Path("../../ASL_output")
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(exist_ok=True)
        
        logger.info(f"ASLGEMINI File Processor initialized")
        logger.info(f"Input directory: {self.input_dir.absolute()}")
        logger.info(f"Output directory: {self.output_dir.absolute()}")
    
    def process_text_file(self, input_file: str) -> Dict[str, Any]:
        """Process a single text file and generate ASL signs"""
        input_path = self.input_dir / input_file
        
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        # Read input text
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read().strip()
        
        logger.info(f"Processing file: {input_file}")
        logger.info(f"Input text: {text}")
        
        # Step 1: Enhance text using Gemini CLI
        enhancement = self.gemini_enhancer.enhance_text_for_signs(text)
        enhanced_text = enhancement.get("enhanced_text", text)
        
        # Step 2: Generate ASL signs using Gemini CLI
        try:
            gemini_signs = self.gemini_enhancer.generate_asl_signs(enhanced_text)
            gemini_available = gemini_signs.get("gemini_used", False)
        except Exception as e:
            logger.warning(f"Gemini API unavailable: {str(e)}")
            gemini_signs = {"signs": [], "gemini_used": False}
            gemini_available = False
        
        # Step 3: Convert to serializable format
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
            sign_sequence = self.sign_language.create_sign_sequence(enhanced_text)
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
        
        # Step 4: Assess quality with Gemini CLI
        quality_assessment = self.gemini_enhancer.assess_sign_quality(enhanced_text, str(serializable_signs))
        
        # Compile results
        results = {
            "input_file": input_file,
            "original_text": text,
            "enhanced_text": enhanced_text,
            "sign_sequence": serializable_signs,
            "enhancement_details": enhancement,
            "gemini_signs_details": gemini_signs,
            "quality_assessment": quality_assessment,
            "gemini_calls": sum([enhancement.get("gemini_used", False), gemini_signs.get("gemini_used", False), quality_assessment.get("gemini_used", False)]),
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "processing_method": "file_based_gemini_cli"
        }
        
        logger.info(f"Generated {len(serializable_signs)} ASL signs")
        logger.info(f"Quality score: {quality_assessment.get('quality_score', 'N/A')}/10")
        
        return results
    
    def save_results(self, results: Dict[str, Any], output_file: str = None) -> str:
        """Save processing results to output file"""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"asl_results_{timestamp}.json"
        
        output_path = self.output_dir / output_file
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Results saved to: {output_path}")
        return str(output_path)
    
    def process_all_files(self) -> List[Dict[str, Any]]:
        """Process all text files in the input directory"""
        input_files = list(self.input_dir.glob("*.txt"))
        
        if not input_files:
            logger.warning("No .txt files found in input directory")
            return []
        
        all_results = []
        
        for input_file in input_files:
            try:
                results = self.process_text_file(input_file.name)
                output_file = f"asl_{input_file.stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                output_path = self.save_results(results, output_file)
                results["output_file"] = output_path
                all_results.append(results)
                
            except Exception as e:
                logger.error(f"Error processing {input_file.name}: {e}")
                error_result = {
                    "input_file": input_file.name,
                    "error": str(e),
                    "success": False,
                    "timestamp": datetime.now().isoformat()
                }
                all_results.append(error_result)
        
        return all_results
    
    def generate_summary_report(self, results: List[Dict[str, Any]]) -> str:
        """Generate a summary report of all processing results"""
        successful = [r for r in results if r.get("success", False)]
        failed = [r for r in results if not r.get("success", False)]
        
        total_gemini_calls = sum(r.get("gemini_calls", 0) for r in successful)
        avg_quality = sum(r.get("quality_assessment", {}).get("quality_score", 0) for r in successful) / len(successful) if successful else 0
        
        report = f"""
# ASL Processing Summary Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Processing Statistics
- Total files processed: {len(results)}
- Successful: {len(successful)}
- Failed: {len(failed)}
- Total Gemini API calls: {total_gemini_calls}
- Average quality score: {avg_quality:.1f}/10

## Successful Processing
"""
        
        for result in successful:
            report += f"""
### {result['input_file']}
- Original: {result['original_text']}
- Enhanced: {result['enhanced_text']}
- Signs generated: {len(result['sign_sequence'])}
- Quality score: {result['quality_assessment'].get('quality_score', 'N/A')}/10
- Output: {result.get('output_file', 'N/A')}
"""
        
        if failed:
            report += "\n## Failed Processing\n"
            for result in failed:
                report += f"- {result['input_file']}: {result.get('error', 'Unknown error')}\n"
        
        return report

# Example usage for testing
if __name__ == "__main__":
    # Test the file processor
    processor = ASLFileProcessor()
    
    # Process all files
    results = processor.process_all_files()
    
    # Generate summary report
    summary = processor.generate_summary_report(results)
    print(summary)
    
    # Save summary report
    summary_file = processor.output_dir / f"processing_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"\nSummary report saved to: {summary_file}")
