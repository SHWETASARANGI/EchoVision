from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class BLIPCaptioner:
    def __init__(self):
        # Initialize the BLIP processor and model
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        # Use GPU if available
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate_caption(self, image_path):
        # Open the image
        image = Image.open(image_path).convert("RGB")
        
        # Process the image
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)
        
        # Generate caption
        out = self.model.generate(**inputs)
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        return caption