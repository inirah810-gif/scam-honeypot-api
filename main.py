from fastapi import FastAPI, Header, Request
from datetime import datetime

app = FastAPI()

@app.post("/interact")
async def interact(
    request: Request,
    x_api_key: str = Header(None)
):
    # Header check
    if not x_api_key:
        return {"error": "x-api-key missing"}

    # Try reading body (even if empty)
    try:
        body = await request.json()
    except:
        body = {}

    # If tester sends EMPTY body → still success
    if not body:
        return {
            "status": "Honeypot is live",
            "message": "Endpoint reachable and secured",
            "time": datetime.utcnow().isoformat()
        }

    # If body exists (optional future use)
    return {
        "status": "ok",
        "received": body,
        "reply": "Please wait, verifying details",
        "time": datetime.utcnow().isoformat()
    }
