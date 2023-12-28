from datetime import datetime

from sqlalchemy import Column, DateTime, Integer


class BaseModelMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
