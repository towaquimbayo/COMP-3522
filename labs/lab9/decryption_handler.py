from start_handler import StartHandler
from des import DesKey
from crypto_mode import CryptoMode


class DecryptionHandler(StartHandler):
    def handle(self, request):
        try:
            if request.encryption_state == CryptoMode.DE:
                key = DesKey(request.key.encode())
                request.result = key.decrypt(request.data_input, padding=True).decode('utf-8')
                return super().handle(request)
        except ValueError:
            print("Error! Wrong key")
        except Exception as e:
            print("Error! Something went wrong:", e)
