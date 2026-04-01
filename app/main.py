from fastapi import FastAPI
from app.routes import router
from app.db import init_db

app = FastAPI(title="Healthcare Symptom Checker")

init_db()

app.include_router(router)
