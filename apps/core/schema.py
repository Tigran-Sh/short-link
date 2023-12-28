from pydantic import BaseModel


class Schema(BaseModel):
    pass


class ModelSchema(BaseModel):

    class Config:
        orm_mode = True
