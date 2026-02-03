from fastapi import FastAPI, Header, Request
from datetime import datetime

app = FastAPI()

@app.post("/interact")
async def interact(request: Request, x_api_key: str = Header(default="")):
    try:
        body = await request.json()
    except:
        body = {}

    return {
        "status": "Honeypot is live",
        "ok": True,
        "api_key_received": bool(x_api_key),
        "body": body,
        "time": datetime.utcnow().isoformat()
    }

@app.get("/")
def root():
    return {"status": "alive"}

