from fastapi import FastAPI
from app.api.v1.endpoints import urls
from app.api import redirect
from app.core.config import settings
from app.db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A simple URL shortener API with stats tracking.",
    version="1.0.0"
)

app.include_router(urls.router, prefix="/api/v1", tags=["urls"])
app.include_router(redirect.router, tags=["redirect"])
