from base_crypt_handler import BaseCryptHandler


class StartHandler(BaseCryptHandler):
    def set_next(self, handler):
        self._next_handler = handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None
