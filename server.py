# This file is inteded for FastAPI Server

from fastapi import FastAPI
from router.whatsapp import wp_router

app = FastAPI()

app.include_router(wp_router)

@app.get("/")
async def read_root():
    return {"message": "Server is running on port 8000"}


