import abc


class BaseCryptHandler(abc.ABC):
    _next_handler = None

    @abc.abstractmethod
    def set_next(self, handler):
        pass

    @abc.abstractmethod
    def handle(self, request):
        pass
