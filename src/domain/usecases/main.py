from src.domain.dto.main import CheckDataDTO, WriteDataDTO
from src.domain.exceptions.main import NotFoundError
from src.domain.usecases.base import BaseUseCase


class WriteDataUseCase(BaseUseCase):
    async def __call__(self, dto: WriteDataDTO) -> None:
        await self._service.set_value(dto.phone, dto.address)


class CheckDataUseCase(BaseUseCase):
    async def __call__(self, dto: CheckDataDTO) -> str:
        address = await self._service.get_value(dto.phone)
        if not address:
            raise NotFoundError
        return address


class Interactor(BaseUseCase):
    async def write_data(self, dto: WriteDataDTO) -> None:
        return await WriteDataUseCase(self._service)(dto)

    async def check_data(self, dto: CheckDataDTO) -> str:
        return await CheckDataUseCase(self._service)(dto)
