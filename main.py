from fastapi import FastAPI, Header, Body
from typing import Optional
from datetime import datetime

app = FastAPI()

# 🔹 Root health check (VERY IMPORTANT)
@app.get("/")
def root():
    return {"status": "Honeypot is live"}

# 🔹 Honeypot interaction endpoint
@app.post("/interact")
def interact(
    data: Optional[dict] = Body(None),
    x_api_key: Optional[str] = Header(None)
):
    if not data:
        return {"status": "Honeypot is live"}

    phone = data.get("phone", "unknown")
    message = data.get("message", "")

    reply = "Sorry sir, konjam clear-ah sollunga."

    if "otp" in message.lower():
        reply = "OTP vandhudhu sir, but phone hang aagudhu."
    elif "bank" in message.lower():
        reply = "Bank verification-na branch la confirm pannalaama?"
    elif "prize" in message.lower():
        reply = "Idhu endha contest sir?"

    return {
        "phone": phone,
        "reply": reply,
        "time": datetime.utcnow()
    }
