import asyncio
from abc import ABC, abstractmethod


class Run(ABC):

    def __init__(self, event):
        self._name = self.__class__.__name__
        self._event = event

    async def __aenter__(self):
        print(f"Initiating {self._name, self._event}")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is not None:
            print(f"Exception {exc_type} in {self._name}. {exc}")
        return True

    async def return_value(self, event):
        print(f"{'True' if event.is_set() else 'False'} from {self._name}")
        await asyncio.sleep(1)

    @abstractmethod
    def task(self, event):
        pass
