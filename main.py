from fastapi import FastAPI, Header, Body
from typing import Optional

app = FastAPI()

@app.post("/interact")
async def interact(
    x_api_key: Optional[str] = Header(None),
    data: Optional[dict] = Body(None)
):
    return {
        "status": "Honeypot is live",
        "received": data
    }

       