from pydantic import BaseModel, HttpUrl, ConfigDict
from datetime import datetime


class URLCreate(BaseModel):
    original_url: HttpUrl


class URLResponse(BaseModel):
    short_id: str
    short_url: str


class URLStats(BaseModel):
    original_url: str
    short_id: str
    clicks: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
