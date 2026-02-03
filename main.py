from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/interact")
async def interact(request: Request):
    try:
        data = await request.json()
    except:
        data = {}

    # 🔑 tester sends empty or broken body → we still respond OK
    if not data:
        return {
            "status": "Honeypot is live"
        }

    return {
        "status": "Honeypot received data",
        "data": data
    }
