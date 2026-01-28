# openapi-voice-convert
```
brew install python@3.10

Python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python app.py
```

tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 --train_data_path dataset/speaker_1 --output_path dataset/finetuned_model --config_path dataset/config