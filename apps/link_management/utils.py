import shortuuid
from sqlalchemy.orm import Session

from apps.core.config import settings
from apps.link_management.services import LinkService


def generate_unique_short_url(db: Session) -> str:
    while True:
        short_url = f'{settings.APP_URL}/{shortuuid.uuid()[:6]}'
        # Check if the short URL already exists in the database
        existing_link = LinkService.get_link_by_short_url(db=db, short_url=short_url)
        if not existing_link:
            return short_url
