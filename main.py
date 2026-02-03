from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "Honeypot is live"}

@app.api_route("/interact", methods=["GET", "POST"])
async def interact(request: Request):
    try:
        data = await request.json()
    except:
        data = {}

    if not data:
        return {
            "status": "Honeypot is live"
        }

    return {
        "status": "Honeypot received data",
        "data": data
    }
