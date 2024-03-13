import uvicorn
from fastapi import FastAPI

from src.vessel.router import router as vessel_router

# initialize the application
app = FastAPI()

# add necessary routers
app.include_router(vessel_router)

# root router
@app.get("/")
async def root():
    return {"message": "Hello World"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
