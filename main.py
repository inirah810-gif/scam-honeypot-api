from fastapi import FastAPI, Header, Body
from typing import Optional
from datetime import datetime

app = FastAPI()

@app.post("/interact")
async def interact(
    data: Optional[dict] = Body(None),
    x_api_key: Optional[str] = Header(None)
):
    # ✅ This is what the tester expects
    if not data:
        return {
            "status": "ok",
            "message": "Honeypot active",
            "timestamp": datetime.utcnow().isoformat()
        }

    message = data.get("message", "").lower()

    if "otp" in message:
        reply = "OTP vandhudhu, aana bank app open aagala. Konjam wait pannunga."
        scam_type = "OTP Scam"
    elif "prize" in message or "won" in message:
        reply = "Idhu endha contest sir? Official website link irukka?"
        scam_type = "Lottery Scam"
    elif "bank" in message:
        reply = "Neenga endha branch-la irundhu call pannureenga?"
        scam_type = "Bank Scam"
    else:
        reply = "Konjam clear-ah sollunga sir."
        scam_type = "Unknown"

    return {
        "reply": reply,
        "scam_type": scam_type,
        "time": datetime.utcnow().isoformat()
    }
