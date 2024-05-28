from start_handler import StartHandler
from crypto_mode import CryptoMode


class DataInputHandler(StartHandler):
    def handle(self, request):
        if request.data_input:
            if ((request.encryption_state == CryptoMode.EN and isinstance(request.data_input, str)) or
                    (request.encryption_state == CryptoMode.DE and isinstance(request.data_input, bytes))):
                return super().handle(request)
        else:
            print("Error! Input file is empty")
