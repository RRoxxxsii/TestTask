from fastapi import FastAPI

from src.presentation.api.controllers.router import router


def setup_controllers(app: FastAPI) -> None:
    app.include_router(router)
