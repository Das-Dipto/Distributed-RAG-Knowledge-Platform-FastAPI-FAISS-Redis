from fastapi import FastAPI

from app.core.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Distributed RAG Platform Running"
    }