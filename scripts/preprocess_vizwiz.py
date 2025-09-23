from datasets import load_dataset
from transformers import BlipProcessor
from PIL import Image

# Load dataset (use subset or full depending on your choice)
dataset = load_dataset("lmms-lab/VizWiz-Caps", split="val[:1%]")

# Initialize BLIP processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

def preprocess(example):
    image = example["image"].convert("RGB")
    caption = example["captions"][0]  # take first caption
    inputs = processor(images=image, text=caption, return_tensors="pt", padding="max_length", max_length=32, truncation=True)
    return inputs

dataset = dataset.map(preprocess, remove_columns=dataset.column_names)
dataset.save_to_disk("data/vizwiz_preprocessed")
print(dataset)