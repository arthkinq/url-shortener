from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.url import URLCreate, URLResponse, URLStats
from app.services.url_service import URLService
from app.repositories.url_repository import URLRepository

router = APIRouter()


def get_url_service(db: Session = Depends(get_db)) -> URLService:
    repository = URLRepository(db)
    return URLService(repository)


@router.post("/urls", response_model=URLResponse, status_code=201)
def create_url(
        url_in: URLCreate,
        request: Request,
        service: URLService = Depends(get_url_service)
):
    db_url = service.create_short_url(str(url_in.original_url))

    base_url = str(request.base_url)
    short_url = f"{base_url}{db_url.short_id}"

    return URLResponse(short_id=db_url.short_id, short_url=short_url)


@router.get("/urls/{short_id}/stats", response_model=URLStats)
def get_stats(
        short_id: str,
        service: URLService = Depends(get_url_service)
):
    db_url = service.get_url_stats(short_id)
    return db_url
