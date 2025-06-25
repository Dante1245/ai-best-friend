
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
from reply_engine import generate_reply
from tts_engine import speak_reply
import requests
import os

app = Flask(__name__)

# Twilio credentials
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_CALLER = os.getenv("TWILIO_CALLER")
MY_PHONE = os.getenv("MY_PHONE")

# UltraMsg credentials
ULTRAMSG_INSTANCE_ID = os.getenv("ULTRAMSG_INSTANCE_ID")
ULTRAMSG_TOKEN = os.getenv("ULTRAMSG_TOKEN")

client = Client(TWILIO_SID, TWILIO_AUTH)

@app.route('/ultramsg', methods=['POST'])
def ultramsg_webhook():
    data = request.json
    incoming_msg = data.get("body", "")
    sender = data.get("from", "")
    reply = generate_reply(incoming_msg)

    url = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE_ID}/messages/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "token": ULTRAMSG_TOKEN,
        "to": sender,
        "body": reply
    }

    requests.post(url, headers=headers, json=payload)
    return "OK"

@app.route('/voice', methods=['POST'])
def voice_reply():
    response = VoiceResponse()
    reply_text = "Hey Steve, just calling to check in. Hope you're doing okay."
    audio_url = speak_reply(reply_text)
    response.play(audio_url)
    return str(response)

@app.route('/')
def index():
    return "Steve's AI Best Friend is online with UltraMsg and Twilio."

if __name__ == "__main__":
    app.run()
