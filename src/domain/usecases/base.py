from src.domain.protocols.inmemory import InMemoryProtocol


class BaseUseCase:
    def __init__(self, service: InMemoryProtocol) -> None:
        self._service = service
