from sqlalchemy import Column, String

from apps.core.db import Base
from apps.core.model import BaseModelMixin


class Link(Base, BaseModelMixin):
    __tablename__ = "links"

    full_url = Column(String(255))
    short_url = Column(String(64), unique=True, index=True)

    def __init__(self, full_url: str, short_url: str):
        self.full_url = full_url
        self.short_url = short_url
