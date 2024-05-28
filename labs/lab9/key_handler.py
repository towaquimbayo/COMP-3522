from start_handler import StartHandler


class KeyHandler(StartHandler):
    def handle(self, request):
        try:
            if len(request.key) in [8, 16, 24]:
                return super().handle(request)
        except Exception as e:
            print("Error! Something went wrong:", e)
