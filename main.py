from fastapi import FastAPI, Header
from typing import Optional
from datetime import datetime

app = FastAPI()
conversation_memory = {}
@app.post("/interact")
async def interact(
    phone: Optional[str] = None,
    message: Optional[str] = None,
    x_api_key: Optional[str] = Header(None)
):
    scam_type = detect_scam_type(message or "")

    # initialize memory
    if phone not in conversation_memory:
        conversation_memory[phone] = {
            "count": 0,
            "scam_type": scam_type
        }

    conversation_memory[phone]["count"] += 1
    step = conversation_memory[phone]["count"]

    # step-based replies
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
        "scam_type": scam_type
    }

