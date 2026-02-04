from fastapi import FastAPI, Header
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/interact")
def interact(x_api_key: str = Header(None)):
    # required header check
    if not x_api_key:
        return {"error": "missing api key"}

    return {
        "status": "success",
        "message": "Honeypot active",
        "reply": "Please wait, I am verifying your details.",
        "timestamp": datetime.utcnow().isoformat()
    }
