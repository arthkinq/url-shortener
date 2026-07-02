from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.url_service import URLService
from app.repositories.url_repository import URLRepository

router = APIRouter()


def get_url_service(db: Session = Depends(get_db)) -> URLService:
    repository = URLRepository(db)
    return URLService(repository)


@router.get("/{short_id}")
def redirect_to_original(
        short_id: str,
        service: URLService = Depends(get_url_service)
):
    original_url = service.get_url_for_redirect(short_id)
    return RedirectResponse(url=original_url, status_code=307)
