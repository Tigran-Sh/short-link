from pydantic import HttpUrl

from apps.core.schema import ModelSchema, Schema


class LinkAddSchema(ModelSchema):
    full_url: HttpUrl


class LinkDeleteSchema(ModelSchema):
    short_url: HttpUrl


class LinkGetSchema(ModelSchema):
    short_url: HttpUrl


class LinkSchema(Schema):
    short_url: HttpUrl
