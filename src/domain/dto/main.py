from dataclasses import dataclass

from src.domain.dto.base import BaseDTO


@dataclass
class WriteDataDTO(BaseDTO):
    phone: str
    address: str


@dataclass
class CheckDataDTO(BaseDTO):
    phone: str
