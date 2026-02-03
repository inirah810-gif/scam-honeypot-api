from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

class MessageRequest(BaseModel):
    phone: str
    message: str

conversation_memory = {}

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
        "OTP scam": [
            "I received the OTP but my phone is updating. Will message you shortly.",
            "OTP came, but it shows different app name. Is that normal?",
            "I’m not very good with phones. Can you explain step-by-step?"
        ],
        "Lottery scam": [
            "Oh wow! Which contest was this from?",
            "Is this related to Amazon or Google?",
            "Do I need to pay any registration fee?"
        ],
        "Banking scam": [
            "I’m outside near ATM. Can you stay on line?",
            "Can you tell last transaction amount to confirm?",
            "SMS is not loading properly on my phone."
        ],
        "Unknown scam": [
            "Sorry, can you explain once more?",
            "I didn’t understand fully. Please clarify."
        ]
    }
    return replies.get(scam_type, ["Please wait..."])[0]

@app.post("/interact")
async def interact(
    data: MessageRequest,
    x_api_key: Optional[str] = Header(None)
):
    phone = data.phone
    message = data.message

    scam_type = detect_scam_type(message)

    if phone not in conversation_memory:
        conversation_memory[phone] = 0

    conversation_memory[phone] += 1
    step = conversation_memory[phone]

    if step == 1:
        reply = ai_reply(scam_type)
    elif step == 2:
        reply = "I’m a bit confused. Can you explain once again?"
    elif step == 3:
        reply = "Before sharing anything, can you confirm your official ID?"
    else:
        reply = "Please wait, I’m checking with my bank."

    return {
        "phone": phone,
        "step": step,
        "reply": reply,
        "scam_type": scam_type,
        "time": datetime.utcnow()
    }
