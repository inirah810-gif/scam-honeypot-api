from fastapi import FastAPI, Header, Body
from typing import Optional
from datetime import datetime

app = FastAPI()

@app.post("/interact")
async def interact(
    payload: Optional[dict] = Body(default={}),
    x_api_key: Optional[str] = Header(None)
):
    return {
        "status": "ok",
        "honeypot": "active",
        "authenticated": True if x_api_key else False,
        "received_body": payload,
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/")
def root():
    return {"status": "alive"}
