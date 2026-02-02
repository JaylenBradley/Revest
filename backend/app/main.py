from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core import settings
from .api import *

app = FastAPI(title=settings.project_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api")
app.include_router(property_router, prefix="/api")