import random
import pyautogui
from .config import Constants


class PointerConstants:
    
    def __init__(self):
        self._constant = Constants()
        self._init_position = self._constant.FISH_POSITION
        self._random_coor = random.choice(list(self._constant.POSITIONS))
        self._tool_selected, self._waiting  = False, False


class Pointer(PointerConstants):

    def __init__(self):
        super().__init__()

    def to_select_click(self):
        pyautogui.click(button='left')
        return self

    def move_to_init(self):
        pyautogui.moveTo(*self._init_position, duration=0.05)
        return self

    def random_position(self):
        pyautogui.moveTo(*self._random_coor, duration=0.05)
        return self
