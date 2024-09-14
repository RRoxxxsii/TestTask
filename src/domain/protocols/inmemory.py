from typing import Protocol


class InMemoryProtocol(Protocol):
    async def set_value(self, key: str, value: str) -> None:
        pass

    async def get_value(self, key: str) -> str | None:
        pass
