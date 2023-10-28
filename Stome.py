import threading
import time
import keyboard
import msvcrt
from concurrent.futures import ThreadPoolExecutor
from Package.ClassStome import Run
from Package.ClassPointer import Pointer


class Fish(Run):

    def task(self, event, shut):
        while not shut.is_set():
            Pointer().random_position()
            event.wait()


class Encase(Run):

    def task(self, event, shut):
        while not shut.is_set():
            is_pressed = keyboard.is_pressed(hotkey="insert")
            if is_pressed and not was_pressed:
                event.clear() if event.is_set() else event.set()
                print("Switch state:", event.is_set())
            was_pressed = is_pressed

            if keyboard.is_pressed(hotkey="ctrl+c"):
                shut.set()
                event.set()

            time.sleep(0.1)


def main():
    halt = threading.Event()
    shut = threading.Event()
    subclasses = [globals()[index.__name__] for index in Run.__subclasses__()]

    with ThreadPoolExecutor(max_workers=len(subclasses)) as executor:
        for Class in subclasses:
            instance = Class(halt, shut)
            with instance:
                executor.submit(instance.task, halt, shut)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        while msvcrt.kbhit():
            msvcrt.getch()
