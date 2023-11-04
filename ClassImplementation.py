import time
import keyboard
from Package.ClassPointer import Pointer
from Package.ClassStome import Run


""" Create new subclasses of Run in this file to execute code in a new thread; 
    Write the desired code inside a function named task() in the respective subclass. """


def threadloop(func):
    """ Decorator to implement the loop, the 'self' or zero return on each thread. """
    def wrapper(*args, **kwargs):
        while not kwargs['shutdown'].is_set():
            func(*args, **kwargs)
        return args[0] if args[0] is not None else 0
    return wrapper


class Info:
    """ Getters from ClassImplementation.py """
    @property
    def get_run_subclasses(self):
        """ Returns all subclasses of Run on a list. """
        return [globals()[index.__name__] for index in Run.__subclasses__()]


class Encase(Run):

    def __init__(self, halt, shutdown):
        super().__init__(halt, shutdown)
        self._was_pressed = False

    @threadloop
    def task(self, halt, shutdown):
        """ Thread to pause or resume all threads. """
        is_pressed = keyboard.is_pressed("insert")
        if is_pressed and not self._was_pressed:
            halt.clear() if halt.is_set() else halt.set()
            print("Switch state:", halt.is_set(), end=' \r')
        self._was_pressed = is_pressed

        if keyboard.is_pressed('escape') or keyboard.is_pressed('ctrl+c'):
            shutdown.set()
            halt.set()
        time.sleep(0.1)


class Fish(Run):

    @threadloop
    def task(self, halt, shutdown):
        """ Main program execution. """
        halt.wait()
        Pointer().random_position()
