from fastapi import FastAPI

from app.core.config.settings import settings
from app.api.v1.routes.documents import router as document_router


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Distributed RAG Platform Running"
    }

app.include_router(document_router, prefix="/api/v1")

// Issue almost detected
