from gtts import gTTS
import os

def text_to_speech(text: str, output_path="data/outputs/output.mp3"):
    """Converts text to speech and saves as MP3"""
    if not text.strip():
        text = "No description available."
    tts = gTTS(text=text, lang="en")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tts.save(output_path)
    print(f"[INFO] Audio saved at {output_path}")