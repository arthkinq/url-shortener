import pytest
from app.services.url_service import URLService
from app.repositories.url_repository import URLRepository
from app.core.exceptions import URLNotFoundException

def test_url_service_create_and_get(db_session):
    repo = URLRepository(db_session)
    service = URLService(repo)
    
    original_url = "https://test.com"
    db_url = service.create_short_url(original_url)
    
    assert db_url.original_url == original_url
    assert len(db_url.short_id) == 6
    assert db_url.clicks == 0
    
    retrieved_url = service.get_url_for_redirect(db_url.short_id)
    assert retrieved_url == original_url
    
    stats = service.get_url_stats(db_url.short_id)
    assert stats.clicks == 1
    
def test_url_service_not_found(db_session):
    repo = URLRepository(db_session)
    service = URLService(repo)
    
    with pytest.raises(URLNotFoundException):
        service.get_url_for_redirect("wrong1")

