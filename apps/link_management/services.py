from typing import Optional

from sqlalchemy.orm import Session

from apps.link_management.models import Link


class LinkService:

    @staticmethod
    def create_link(db: Session, data: dict) -> dict:
        link = Link(
            full_url=data.get('full_url'),
            short_url=data.get('short_url')
        )
        db.add(link)
        db.commit()
        db.refresh(link)
        return link.__dict__

    @staticmethod
    def get_link_by_short_url(db: Session, short_url: str) -> Optional[Link]:
        link = db.query(Link).filter(Link.short_url == short_url).first()
        return link

    @staticmethod
    def delete_link(db: Session, link: Link):
        db.delete(link)
        db.commit()

