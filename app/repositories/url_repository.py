from sqlalchemy.orm import Session
from app.db.models import URL
from typing import Optional


class URLRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_short_id(self, short_id: str) -> Optional[URL]:
        return self.db.query(URL).filter(URL.short_id == short_id).first()

    def create(self, original_url: str, short_id: str) -> URL:
        db_url = URL(original_url=original_url, short_id=short_id)
        self.db.add(db_url)
        self.db.commit()
        self.db.refresh(db_url)
        return db_url

    def increment_clicks(self, db_url: URL) -> None:
        db_url.clicks += 1
        self.db.commit()
        self.db.refresh(db_url)
