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

    text = "Once upon a time, there was a crow who was very thirsty after flying for a long time under the hot sun. His throat was dry and he felt weak, so he searched everywhere for water. After a while, he noticed a pot with a little water at the bottom, but the level was too low for him to reach with his beak. Instead of giving up, the clever crow thought of an idea and began dropping small stones into the pot one by one. Slowly, the water level rose, allowing him to drink. Feeling refreshed and happy, the crow flew away, having solved his problem through intelligence and patience."

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
