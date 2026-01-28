from TTS.api import TTS
import os

MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"

VOICES = {
    "speaker_1": "dataset/speaker_1/saurabh.wav"
}

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("Loading XTTS model...")
    tts = TTS(MODEL_NAME)

    text = "Welcome to the team ! Hoshiyar & Kaushik"

    for speaker, wav_path in VOICES.items():
        print(f"Generating voice for: {speaker}")

        output_path = os.path.join(OUTPUT_DIR, f"{speaker}_output.wav")

        tts.tts_to_file(
            text=text,
            speaker_wav=wav_path,
            language="en",      # 🔥 REQUIRED
            file_path=output_path
        )

        print(f"Saved: {output_path}")

    print("Done ✅")

if __name__ == "__main__":
    main()