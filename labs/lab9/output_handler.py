from start_handler import StartHandler
from crypto_mode import CryptoMode


class OutputHandler(StartHandler):
    def handle(self, request):
        try:
            if request.output == "print":
                print(request.result)
            else:
                if request.encryption_state == CryptoMode.DE:
                    with open(request.output, "w") as f:
                        f.write(request.result)
                elif request.encryption_state == CryptoMode.EN:
                    with open(request.output, "wb") as f:
                        f.write(request.result)
        except Exception as e:
            print("Error! Something went wrong:", e)
