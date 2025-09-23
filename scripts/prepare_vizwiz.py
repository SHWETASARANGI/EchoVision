from datasets import load_dataset
import os
from PIL import Image

# Step 1: Download VizWiz dataset (Captions)
print("[INFO] Downloading VizWiz Captions dataset...")
dataset = load_dataset("lmms-lab/VizWiz-Caps", split="val[:1%]")  # small subset
print(f"[INFO] Dataset loaded with {len(dataset)} samples.")
print(dataset[0])

output_dir = "data/vizwiz"
os.makedirs(output_dir, exist_ok=True)


sample = dataset[0]
print("[SAMPLE DATA]")
print("Caption:", sample["caption"])
print("Image:", sample["image"])


for i in range(5):  # save first 5 images only
    img = dataset[i]["image"]
    caption = dataset[i]["caption"]

    save_path = os.path.join(output_dir, f"sample_{i}.jpg")
    img.save(save_path)

    with open(os.path.join(output_dir, f"sample_{i}.txt"), "w") as f:
        f.write(caption)

print(f"[INFO] Saved {5} sample images + captions in {output_dir}")