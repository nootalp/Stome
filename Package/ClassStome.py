from abc import ABC, abstractmethod
import time


class Run(ABC):

    def __init__(self, event, shut):
        self._name = self.__class__.__name__
        self._event = event
        self._shut = shut

    def __enter__(self):
        print(f"Initiating {self._name, self._event, self._shut}")
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None:
            print(f"Exception {exc_type} in {self._name}. {exc}")
        return True

    def return_value(self, event):
        print(f"{'True' if event.is_set() else 'False'} from {self._name}")
        time.sleep(1)

    @abstractmethod
    def task(self, event, shut):
        raise NotImplementedError("Subclasses must implement this method.")
