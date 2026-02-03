from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI()

@app.post("/interact")
async def interact(x_api_key: Optional[str] = Header(None)):
    return {"status": "Honeypot is live"}

       