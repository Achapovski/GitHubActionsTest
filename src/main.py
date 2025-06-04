from fastapi import FastAPI

app = FastAPI()


@app.get("/health_check")
async def heal_check():
    return {"status": "ok"}


@app.get("/")
async def welcome():
    return {"message": "Welcome"}
