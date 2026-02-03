from fastapi import FastAPI, Header, Request
from datetime import datetime

app = FastAPI()

@app.post("/interact")
async def interact(
    request: Request,
    x_api_key: str = Header(None)
):
    try:
        body = await request.json()
    except:
        body = {}

    # Tester empty body anuppinaalum accept pannanum
    if not body:
        return {
            "status": "Honeypot is live",
            "time": datetime.utcnow().isoformat()
        }

    phone = body.get("phone", "unknown")
    message = body.get("message", "")

    return {
        "phone": phone,
        "reply": "Please wait, this call is being verified.",
        "logged": True,
        "time": datetime.utcnow().isoformat()
    }
