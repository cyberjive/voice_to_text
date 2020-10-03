## Twilio: Voice to Text

Code from Twilio Blog post: <a href="https://www.twilio.com/blog/transcribe-voicemails-python-flask-twilio">Transcribe your voicemails with Python, Flask, and Twilio</a>

A simple Flask app to record an incoming phonecall and email the transcription.

## Installation

Clone, create your venv, install dependencies

```bash
git clone https://github.com/cyberjive/voice_to_text.git
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

## Usage

Activate your virtual environment and run the app via the CLI or your IDE of choice.


```bash
source env/bin/activate
python3 record_incoming_voice.py
```