#!/usr/bin/env python3
"""
ASLGEMINI File Processing Script for Hackathon
Demonstrates local file processing with Gemini CLI integration
"""

import os
import sys
from pathlib import Path

# Add src directory to path
sys.path.append(str(Path(__file__).parent / "src"))

from file_processor import ASLGEMINIFileProcessor

def main():
    """Main function to process ASL input files"""
    print("🤟 ASLGEMINI File Processing with Gemini CLI")
    print("=" * 50)
    
    # Set up environment
    if not os.getenv('GEMINI_API_KEY'):
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        print("Please set your Gemini API key:")
        print("export GEMINI_API_KEY=your_api_key_here")
        return 1
    
    try:
        # Initialize processor
        processor = ASLGEMINIFileProcessor()
        
        # Process all files
        print(f"📁 Input directory: {processor.input_dir.absolute()}")
        print(f"📁 Output directory: {processor.output_dir.absolute()}")
        print()
        
        results = processor.process_all_files()
        
        if not results:
            print("⚠️ No files found to process")
            return 0
        
        # Generate summary report
        summary = processor.generate_summary_report(results)
        print(summary)
        
        # Save summary report
        summary_file = processor.output_dir / f"processing_summary_{processor.gemini_enhancer.__class__.__name__}_{len(results)}_files.md"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        print(f"\n📄 Summary report saved to: {summary_file}")
        
        # Show success
        successful = [r for r in results if r.get("success", False)]
        print(f"\n✅ Successfully processed {len(successful)}/{len(results)} files")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
