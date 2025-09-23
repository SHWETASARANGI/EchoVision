from PIL import Image
import os

def load_image(image_path: str):
    """Load an image safely and return it as a PIL Image."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    try:
        image = Image.open(image_path).convert("RGB")
        return image
    except Exception as e:
        raise RuntimeError(f"Error loading image: {e}")