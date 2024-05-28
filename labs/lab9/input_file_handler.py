from crypto_mode import CryptoMode
from start_handler import StartHandler


class InputFileHandler(StartHandler):
    def handle(self, request):
        if request.input_file:
            if request.encryption_state == CryptoMode.DE:
                with open(request.input_file, "rb") as f:
                    request.data_input = f.read()
            elif request.encryption_state == CryptoMode.EN:
                with open(request.input_file, "r") as f:
                    request.data_input = f.read()
            return super().handle(request)
        elif request.data_input:
            return super().handle(request)
        else:
            print("Error! Input file is empty")
