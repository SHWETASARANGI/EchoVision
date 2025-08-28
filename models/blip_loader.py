from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

class BLIPCaptioner:
    def _init_(self, model_name="Salesforce/blip-image-captioning-base"):
        print("[INFO] Loading BLIP model...")
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)

    def generate_caption(self, image_path: str) -> str:
        """Generates a caption for the given image"""
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt")
        out = self.model.generate(**inputs)
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        return caption