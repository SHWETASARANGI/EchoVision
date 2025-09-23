from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class BLIPCaptioner:
    def _init_(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

        # ✅ Device preference: MPS > CUDA > CPU
        if torch.backends.mps.is_available():
            self.device = torch.device("mps")
            print("[INFO] Using Apple MPS GPU 🚀")
        elif torch.cuda.is_available():
            self.device = torch.device("cuda")
            print("[INFO] Using NVIDIA CUDA GPU 🚀")
        else:
            self.device = torch.device("cpu")
            print("[INFO] Using CPU 🐢")

        self.model.to(self.device)

    def generate_caption(self, image):
        """
        Generate caption for an image.
        Accepts either a file path (str) or a PIL.Image.
        """
        if isinstance(image, str):  # if path given
            image = Image.open(image).convert("RGB")

        inputs = self.processor(images=image, return_tensors="pt").to(self.device)

        with torch.inference_mode():
            out = self.model.generate(**inputs, max_new_tokens=50)

        caption = self.processor.decode(out[0], skip_special_tokens=True)
        return caption