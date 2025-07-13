# This file is inteded for FastAPI Server

from fastapi import FastAPI
from router.whatsapp import wp_router
from contextlib import asynccontextmanager
from shopify.fetch_products import get_all_shopify_products

@asynccontextmanager
async def lifespan(app: FastAPI):
    get_all_shopify_products()
    yield

    print("Server is shutting down!")

app = FastAPI(lifespan=lifespan)
app.include_router(wp_router)

@app.get("/")
async def read_root():
    return {"message": "Server is running on port 8000"}



