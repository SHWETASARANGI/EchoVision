import sys
import os

# Make sure Python can find the project root (so imports work)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.blip_loader import BLIPCaptioner
from models.ocr_engine import OCREngine
from utils.audio_utils import text_to_speech


if __name__ == "__main__":
    image_path = r"C:\Users\sweta\OneDrive\Desktop\EchoVision\EchoVision\data\samples\sample.jpeg"

    # Step 1: Image Captioning
    blip = BLIPCaptioner()
    caption = blip.generate_caption (r"C:\Users\sweta\OneDrive\Desktop\EchoVision\EchoVision\data\samples\sample.jpeg")
    print("[CAPTION] ", caption)

    # Step 2: OCR Text Extraction
    ocr = OCREngine()
    text = ocr.extract_text(r"C:\Users\sweta\OneDrive\Desktop\EchoVision\EchoVision\data\samples\sample.jpeg")
    print("[OCR TEXT] ", text)

    # Step 3: Merge results & Convert to Audio
    final_text = caption + " " + text
    text_to_speech(final_text, "data/outputs/summary.mp3")