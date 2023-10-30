from abc import ABC, abstractmethod
import time


class Run(ABC):

    def __init__(self, halt, shutdown):
        self._name = self.__class__.__name__
        self._halt = halt
        self._shutdown = shutdown

    def __enter__(self):
        print(f"Initiating {self._name, self._halt, self._shutdown}")
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None:
            print(f"Exception {exc_type} in {self._name}. {exc}")
        return True

    def return_value(self, halt):
        print(f"{'True' if halt.is_set() else 'False'} from {self._name}")
        time.sleep(1)

    @abstractmethod
    def task(self, halt, shutdown):
        raise NotImplementedError("Subclasses must implement this method.")
