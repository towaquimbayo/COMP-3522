from start_handler import StartHandler
from des import DesKey
from crypto_mode import CryptoMode


class EncryptionHandler(StartHandler):
    def handle(self, request):
        try:
            if request.encryption_state == CryptoMode.EN:
                key = DesKey(request.key.encode())
                request.result = key.encrypt(request.data_input.encode(), padding=True)

                return super().handle(request)
        except ValueError:
            print("Error! Wrong key")
        except Exception as e:
            print("Error! Something went wrong:", e)
