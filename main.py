from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Honeypot is live"}

@app.get("/interact")
def interact(
    phone: str = Query(None),
    message: str = Query(None)
):
    # If tester sends empty request
    if not phone or not message:
        return {
            "status": "Honeypot is live",
            "note": "Waiting for attacker input"
        }

    return {
        "phone": phone,
        "received_message": message,
        "ai_reply": "Please wait, I am verifying your details.",
        "time": datetime.utcnow().isoformat()
    }
