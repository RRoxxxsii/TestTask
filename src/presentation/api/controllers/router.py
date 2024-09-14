from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import Response

from src.domain.dto.main import CheckDataDTO, WriteDataDTO
from src.domain.exceptions.main import NotFoundError
from src.domain.usecases.main import Interactor
from src.presentation.api.controllers.requests import WriteDataSchema
from src.presentation.api.controllers.responses import (
    CheckDataResponse,
    NotFoundResponse,
    OkResponse,
)
from src.presentation.api.di.services import get_service

router = APIRouter(prefix="", tags=["Main"])


@router.put(
    "/write_data/",
    status_code=status.HTTP_201_CREATED,
    summary="Создание или обновление"
)
async def write_data(
    schema: WriteDataSchema, service: Interactor = Depends(get_service)
) -> OkResponse:
    await service.write_data(WriteDataDTO(**schema.model_dump()))
    return OkResponse()


@router.get(
    "/check_data",
    status_code=status.HTTP_200_OK,
    summary="Получить адрес",
    responses={
        status.HTTP_200_OK: {
            "description": "ok",
            "content": {
                "application/json": {
                    "example": {"address": "ул. Ленина, д. 1"}
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "not found",
            "content": {
                "application/json": {
                    "example": {"status": "not_found"}
                }
            }
        }
    }
)
async def check_data(
    phone: str,
    response: Response,
    service: Interactor = Depends(get_service),
) -> CheckDataResponse | NotFoundResponse:
    try:
        address = await service.check_data(CheckDataDTO(phone=phone))
    except NotFoundError:
        response.status_code = status.HTTP_404_NOT_FOUND
        return NotFoundResponse()
    else:
        response.status_code = status.HTTP_200_OK
        return CheckDataResponse(address=address)
