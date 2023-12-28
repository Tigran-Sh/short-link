import logging

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from apps.core.config import settings
from apps.core.db_utils import get_db
from apps.link_management.schemas import LinkAddSchema, LinkDeleteSchema, LinkSchema
from apps.link_management.services import LinkService
from apps.link_management.utils import generate_unique_short_url

link_routes = APIRouter()
redirect_rout = APIRouter()

logger = logging.getLogger(__name__)


@redirect_rout.get(
    "/{short_url}", status_code=status.HTTP_301_MOVED_PERMANENTLY, responses={
        status.HTTP_404_NOT_FOUND: {"description": "Link not found"}
    }
)
def get_link(short_url: str, db: Session = Depends(get_db)):
    short_url = f'{settings.APP_URL}/{short_url}'
    link = LinkService.get_link_by_short_url(db, short_url)
    if link:
        return RedirectResponse(
            url=str(link.full_url), status_code=status.HTTP_301_MOVED_PERMANENTLY
        )
    raise HTTPException(status_code=404, detail="Link not found")


@link_routes.post("/", response_model=LinkSchema, status_code=status.HTTP_201_CREATED)
def create_link(payload: LinkAddSchema, db: Session = Depends(get_db)):
    full_url = payload.full_url
    short_url = generate_unique_short_url(db)
    data = {
        'full_url': str(full_url),
        'short_url': short_url
    }
    link = LinkService.create_link(db=db, data=data)
    return LinkSchema(**link)


@link_routes.delete(
    "/{short_url}", status_code=status.HTTP_200_OK, responses={
        status.HTTP_404_NOT_FOUND: {"description": "Link not found"}
    }
)
def delete_link(payload: LinkDeleteSchema, db: Session = Depends(get_db)):
    short_link = str(payload.short_url)
    link = LinkService.get_link_by_short_url(db, short_link)

    if link:
        LinkService.delete_link(db, link)
        return {'status': status.HTTP_200_OK}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")
