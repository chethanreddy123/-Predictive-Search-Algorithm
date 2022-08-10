from fastapi import FastAPI, Request

app =  FastAPI()

@app.post("/username")
async def GetUserName(info : Request):
    req_info = await info.json()
    print(info.cookies)

    return req_info