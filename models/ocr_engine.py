import easyocr
from PIL import Image
import numpy as np

class OCREngine:
    def _init_(self):
        self.reader = easyocr.Reader(['en'], gpu=False)

    def extract_text(self, image):
        """
        Extracts text from an image.
        Accepts either a file path (str) or a PIL.Image.
        """
        if isinstance(image, Image.Image):  # if PIL image
            image = np.array(image)  # easyocr needs numpy array

        results = self.reader.readtext(image)
        extracted_text = " ".join([res[1] for res in results])
        return extracted_text