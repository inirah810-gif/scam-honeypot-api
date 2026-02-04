from fastapi import FastAPI, Header
from datetime import datetime

app = FastAPI()

@app.post("/")
async def honeypot_root(x_api_key: str = Header(None)):
    return {
        "status": "Honeypot active",
        "mode": "agentic",
        "message": "Scammer interaction simulated successfully",
        "timestamp": datetime.utcnow().isoformat()
    }
