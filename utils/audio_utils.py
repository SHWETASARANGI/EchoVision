from gtts import gTTS
import pyttsx3
import os
import platform
import subprocess

def text_to_speech(text: str, output_path="data/outputs/output.mp3", mode="online", play=True):
    """
    Converts text to speech and saves as audio.
    
    Args:
        text (str): The text to convert.
        output_path (str): File path to save audio.
        mode (str): "online" (gTTS) or "offline" (pyttsx3).
        play (bool): If True, play audio after saving.
    """
    if not text.strip():
        text = "No description available."

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if mode == "online":
        # ✅ Google TTS (MP3, requires internet)
        if not output_path.endswith(".mp3"):
            output_path = output_path.rsplit(".", 1)[0] + ".mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(output_path)

    elif mode == "offline":
        # ✅ Offline TTS (WAV)
        if not output_path.endswith(".wav"):
            output_path = output_path.rsplit(".", 1)[0] + ".wav"
        engine = pyttsx3.init()
        engine.save_to_file(text, output_path)
        engine.runAndWait()

    else:
        raise ValueError("Invalid mode. Choose 'online' or 'offline'.")

    print(f"[INFO] Audio saved at {output_path}")

    # ✅ Play audio if requested
    if play:
        system = platform.system()
        try:
            if system == "Darwin":  # macOS
                subprocess.run(["afplay", output_path])
            elif system == "Windows":
                os.startfile(output_path)
            elif system == "Linux":
                subprocess.run(["xdg-open", output_path])
        except Exception as e:
            print(f"[WARN] Could not play audio automatically: {e}")

    return output_path