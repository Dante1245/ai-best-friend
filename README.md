
# Steve's AI Best Friend with UltraMsg

## Features:
- WhatsApp messaging using UltraMsg
- Voice call replies using Twilio and ElevenLabs
- Emotional memory and goal tracking

## Environment Variables:
- TWILIO_SID
- TWILIO_AUTH
- TWILIO_CALLER
- MY_PHONE
- ELEVENLABS_API_KEY
- ELEVENLABS_VOICE_ID
- ULTRAMSG_INSTANCE_ID
- ULTRAMSG_TOKEN

## Deploy on Render:
- Build command: pip install -r requirements.txt
- Start command: gunicorn app:app

## Webhook URLs:
- WhatsApp: /ultramsg
- Voice: /voice
