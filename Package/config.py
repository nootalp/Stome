import threading


class Constants:
    def __init__(self):
        self._name = self.__class__.__name__
        self.HALT = threading.Event()
        self.SHUTDOWN = threading.Event()
        self.FISH_POSITION = (484, 333)
        self.POSITIONS = {
            (460, 349),
            (400, 406),
            (462, 288),
            (401, 528),
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f'Exception {exc_type} in {self._name}. {exc_value}\n{traceback}')
