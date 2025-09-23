import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Import your pipeline modules
from models.blip_loader import BLIPCaptioner
from models.ocr_engine import OCREngine
from utils.audio_utils import text_to_speech
from utils.image_utils import load_image

# Flask app setup
app = Flask(_name_)
UPLOAD_FOLDER = "data/uploads"
OUTPUT_FOLDER = "data/outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load models once
blip = BLIPCaptioner()
ocr = OCREngine()

@app.route("/")
def index():
    """Landing page (upload form)."""
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    """Handles image upload and runs pipeline."""
    if "file" not in request.files:
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("index"))

    # Save uploaded image
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Step 1: Generate caption
    caption = blip.generate_caption(file_path)

    # Step 2: OCR text
    text = ocr.extract_text(file_path)

    # Step 3: Merge
    final_text = caption + " " + text

    # Step 4: Convert to audio
    audio_path = os.path.join(OUTPUT_FOLDER, "summary.mp3")
    text_to_speech(final_text, audio_path)

    # Send result to result.html
    return render_template("result.html",
                           caption=caption,
                           ocr_text=text,
                           final_text=final_text,
                           audio_file=audio_path)

if _name_ == "_main_":
    app.run(debug=True)
