class InvalidDataError(Exception):
    def __init__(self, message):
        """
        Creates an InvalidDataError object.
        :param message: Error message
        """
        super().__init__(message)
