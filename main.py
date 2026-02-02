from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Agentic Scam Honeypot")

class ScamInput(BaseModel):
    phone: str
    message: str

@app.get("/")
def root():
    return {"status": "Honeypot is live"}

@app.post("/honeypot/message")
def honeypot(data: ScamInput):
    text = data.message.lower()

    scam_type = "unknown"
    if "otp" in text:
        scam_type = "OTP scam"
    elif "loan" in text:
        scam_type = "Loan scam"
    elif "prize" in text or "won" in text:
        scam_type = "Prize scam"

    return {
        "reply": "Please wait, our agent will verify your details.",
        "scam_type": scam_type,
        "received_at": datetime.utcnow()
    }
