from fastapi import FastAPI, Header
from typing import Optional
from datetime import datetime

app = FastAPI()

def detect_scam_type(message: str):
    msg = message.lower()
    if "otp" in msg:
        return "OTP scam"
    if "won" in msg or "prize" in msg:
        return "Lottery scam"
    if "bank" in msg or "account" in msg:
        return "Banking scam"
    return "Unknown scam"

def ai_reply(scam_type: str):
    replies = {
        "OTP scam": "I just got the message. My phone battery is low, can I send it in 10 minutes?",
        "Lottery scam": "Oh really? I didn’t apply anywhere. Which company is this from?",
        "Banking scam": "I am outside right now. Can you tell me last 3 digits of my account to confirm?",
        "Unknown scam": "Sorry, I’m a bit confused. Can you explain once again?"
    }
    return replies.get(scam_type, "Please wait, I am checking.")

@app.post("/interact")
async def interact(message: Optional[str] = None, x_api_key: Optional[str] = Header(None)):
    scam_type = detect_scam_type(message or "")
    reply = ai_reply(scam_type)

    return {
        "reply": reply,
        "scam_type": scam_type,
        "received_at": datetime.utcnow()
    }
