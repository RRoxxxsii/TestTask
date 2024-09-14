from pydantic import BaseModel, Field


class CheckDataResponse(BaseModel):
    address: str


class OkResponse(BaseModel):
    status: str = Field("ok")


class NotFoundResponse(BaseModel):
    status: str = Field("not_found")
