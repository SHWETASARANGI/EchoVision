import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Import your model + OCR + TTS utils
from utils.blip_loader import generate_caption
from utils.ocr_engine import OCREngine
from utils.audio_utils import text_to_speech

app = Flask(__name__)

# Config
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Initialize OCR engine once
ocr_engine = OCREngine()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("index"))

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        #  Step 1: Generate caption from BLIP
        caption = generate_caption(filepath)

        # Step 2: Extract text (OCR)
        extracted_text = ocr_engine.extract_text(filepath)

        #  Step 3: Combine both
        summary = caption
        if extracted_text:
            summary += f" The image also contains the text: {extracted_text}"

        # step 4: Generate audio
        audio_file_rel = os.path.join("uploads", "summary.mp3")
        audio_file_path = os.path.join(app.config["UPLOAD_FOLDER"], "summary.mp3")
        text_to_speech(summary, output_path=audio_file_path, mode="online", play=False)

        return render_template(
            "result.html",
            summary=summary,
            filename=filename,
            audio_file=audio_file_rel,
        )

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)