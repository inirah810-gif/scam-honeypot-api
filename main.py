from fastapi import FastAPI, Header, Request
from datetime import datetime

app = FastAPI()

@app.post("/interact")
async def interact(request: Request, x_api_key: str = Header(None)):
    return {
        "status": "Honeypot is live",
        "authenticated": x_api_key is not None,
        "time": datetime.utcnow().isoformat()
    }

@app.get("/")
def root():
    return {"status": "ok"}
