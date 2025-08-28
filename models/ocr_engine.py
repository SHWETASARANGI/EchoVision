import easyocr

class OCREngine:
    def _init_(self, lang_list=["en"]):
        print("[INFO] Initializing OCR...")
        self.reader = easyocr.Reader(lang_list)

    def extract_text(self, image_path: str) -> str:
        """Extracts text from image using EasyOCR"""
        results = self.reader.readtext(image_path, detail=0)
        return " ".join(results) if results else "No text detected."