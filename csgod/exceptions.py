class CSGOdError(Exception):
    pass


class GameNotInstalledError(CSGOdError):
    pass


class InvalidHookFileError(CSGOdError, ):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
