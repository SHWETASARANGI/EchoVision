import easyocr

class OCREngine:
    def __init__(self):
        # Initialize the OCR reader (English language)
        self.reader = easyocr.Reader(['en'], gpu=False)  # set gpu=True if you have CUDA

    def extract_text(self, image_path):
        # Run OCR on the image
        results = self.reader.readtext(image_path)
        
        # Combine all detected text
        extracted_text = " ".join([res[1] for res in results])
        return extracted_text