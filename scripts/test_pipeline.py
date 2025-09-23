import sys
import os

# Ensure project root is in Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(_file_))))

from models.blip_loader import BLIPCaptioner
from models.ocr_engine import OCREngine
from utils.audio_utils import text_to_speech
from utils.image_utils import load_image


def main():
    #  Update this path to your sample image
    image_path = "data/samples/sample1.jpeg"

    # Step 1: Load Image
    image = load_image(image_path)

    # Step 2: Generate Caption
    blip = BLIPCaptioner()
    caption = blip.generate_caption(image_path)
    print("[CAPTION]", caption)

    # Step 3: OCR Text Extraction
    ocr = OCREngine()
    text = ocr.extract_text(image_path)
    print("[OCR TEXT]", text)

    # Step 4: Merge results & Convert to Audio
    final_text = caption + " " + text
    text_to_speech(final_text, "data/outputs/summary.mp3")
    print("[INFO] Pipeline complete ")


if __name__ == "__main__":
    main()