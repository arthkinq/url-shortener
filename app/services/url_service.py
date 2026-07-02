from sqlalchemy.exc import IntegrityError
from app.repositories.url_repository import URLRepository
from app.utils.base62 import generate_random_short_id
from app.core.exceptions import URLNotFoundException
from app.db.models import URL


class URLService:
    def __init__(self, repository: URLRepository):
        self.repository = repository

    def create_short_url(self, original_url: str) -> URL:
        max_retries = 5
        for _ in range(max_retries):
            short_id = generate_random_short_id()
            try:
                return self.repository.create(original_url=original_url, short_id=short_id)
            except IntegrityError:
                self.repository.db.rollback()
                continue
        raise Exception("Failed to generate a unique short ID after multiple attempts")

    def get_url_for_redirect(self, short_id: str) -> str:
        db_url = self.repository.get_by_short_id(short_id)
        if not db_url:
            raise URLNotFoundException()

        self.repository.increment_clicks(db_url)
        return db_url.original_url

    def get_url_stats(self, short_id: str) -> URL:
        db_url = self.repository.get_by_short_id(short_id)
        if not db_url:
            raise URLNotFoundException()
        return db_url
