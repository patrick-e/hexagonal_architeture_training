from fastapi import FastAPI
from app.api.routes import routedeveloper

app = FastAPI()

app.include_router(routedeveloper.router, prefix="/api/v1")