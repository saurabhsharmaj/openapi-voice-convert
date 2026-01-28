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

    text = "टीम विच तुहाड़ा स्वागत है"



    for speaker, wav_path in VOICES.items():
        output_path = os.path.join(OUTPUT_DIR, f"{speaker}_pa.wav")

        tts.tts_to_file(
            text=text,
            speaker_wav=wav_path,
            language="hi",      # ✅ Punjabi
            file_path="outputs/speaker_1_pa.wav"
        )

        print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()
