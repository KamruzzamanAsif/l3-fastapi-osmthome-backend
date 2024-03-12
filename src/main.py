import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)