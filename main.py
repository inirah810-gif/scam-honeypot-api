from fastapi import FastAPI, Header
from datetime import datetime

app = FastAPI()

@app.post("/interact")
async def interact(x_api_key: str = Header(None)):
    return {
        "status": "success",
        "honeypot": "active",
        "timestamp": datetime.utcnow().isoformat()
    }
