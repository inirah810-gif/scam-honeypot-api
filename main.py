from fastapi import FastAPI, Header, Body
from typing import Optional
from datetime import datetime

app = FastAPI()

conversation_memory = {}

def detect_scam_type(message: str):
    msg = (message or "").lower()
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
def generate_scam_reply(stage: str):
    replies = {
        "initial": "Sorry sir, konjam clear ah sollunga.",
        "middle": "Bank change aachunu message vandhuchu, idhu related ah?",
        "advanced": "Neenga endha department sir? Cyber cell verification ah?",
        "end": "Conversation logged. Cyber crime team notified."
    }
    return replies.get(stage, "Please explain again.")

@app.post("/interact")
async def interact(
    data: Optional[dict] = Body(None),
    x_api_key: Optional[str] = Header(None)
):
    # if platform sends empty body
    if not data:
        return {"status": "Honeypot is live"}

    phone = data.get("phone")
    message = data.get("message")

    if not phone or not message:
        return {"error": "phone and message required"}

    scam_type = detect_scam_type(message)

    if phone not in conversation_memory:
        conversation_memory[phone] = 0

    conversation_memory[phone] += 1
    step = conversation_memory[phone]

   if step == 1:
    reply = generate_scam_reply("initial")
elif step == 2:
    reply = generate_scam_reply("middle")
elif step == 3:
    reply = generate_scam_reply("advanced")
else:
    reply = generate_scam_reply("end")

    return {
        "phone": phone,
        "step": step,
        "reply": reply,
        "scam_type": scam_type,
        "time": datetime.utcnow()
    }
