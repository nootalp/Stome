from .common import Constants
import random
import pyautogui
import time


class Pointer:

    def __init__(self):
        self._init_position = Constants.FISH_POSITION
        self._random_coor = random.choice(list(Constants.POSITIONS))
        self._current_position = pyautogui.position()
        self._tool_selected = False
        self._waiting = False

    @staticmethod
    def to_select_click():
        pyautogui.click(button='left')

    def move_to_init(self):
        pyautogui.moveTo(*self._init_position, duration=0.05)

    def random_position(self):
        pyautogui.moveTo(*self._random_coor, duration=0.05)

    @staticmethod
    def is_green_fish(current_x, current_y, check_interval=0.1):
        prev_color = pyautogui.pixel(current_x, current_y)

        while True:
            current_color = pyautogui.pixel(current_x, current_y)
            if current_color != prev_color:
                return True
            prev_color = current_color
            time.sleep(check_interval)

    def perform_action_sequence(self, action_list):
        self._tool_selected = True
        for action in action_list:
            action()
        self._tool_selected = False
        self.move_to_init()

    def full_cicle(self):
        action_list = [self.to_select_click, self.random_position, self.to_select_click]
        self.perform_action_sequence(action_list)

    def choose_position(self):
        action_list = [self.random_position, self.to_select_click]
        self.perform_action_sequence(action_list)

    def perform_logic(self):
        self.move_to_init()

        if self._waiting and self.is_green_fish(*self._init_position):
            self.to_select_click()
            time.sleep(random.expovariate(1.0 / 0.1))
            self._waiting = False
        else:
            self.full_cicle()
            self._waiting = True

        time.sleep(0.5)
