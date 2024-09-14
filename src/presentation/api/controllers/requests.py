from pydantic import BaseModel


class WriteDataSchema(BaseModel):
    phone: str
    address: str
