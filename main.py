from fastapi import FastAPI
from routes.json_placeholders import router

app = FastAPI()

app.include_router(router, prefix="/json-placeholders")