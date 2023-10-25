from config import Constants
import random, pyautogui, asyncio


class Pointer:

    def __init__(self):
        self._init_position = Constants.FISH_POSITION
        self._random_coor = random.choice(list(Constants.POSITIONS))
        self._current_position = pyautogui.position()
        self._tool_selected = False
        self._waiting = False

    @staticmethod
    async def to_select_click():
        pyautogui.click(button='left')

    async def move_to_init(self):
        pyautogui.moveTo(*self._init_position, duration=0.05)

    async def random_position(self):
        pyautogui.moveTo(*self._random_coor, duration=0.05)

    @staticmethod
    async def is_green_fish(current_x, current_y, check_interval=0.1):
        prev_color = pyautogui.pixel(current_x, current_y)

        while True:
            current_color = pyautogui.pixel(current_x, current_y)
            if current_color != prev_color:
                return True
            prev_color = current_color
            await asyncio.sleep(check_interval)

    async def perform_action_sequence(self, action_list):
        self._tool_selected = True
        await asyncio.gather(*[action() for action in action_list])
        self._tool_selected = False
        await self.move_to_init()

    async def full_cicle(self):
        # Inicie as ações em action_list.
        action_list = [self.to_select_click, self.random_position, self.to_select_click]
        await self.perform_action_sequence(action_list)

    async def choose_position(self):
        # Inicie as ações em action_list.
        action_list = [self.random_position, self.to_select_click]
        await self.perform_action_sequence(action_list)

    async def perform_logic(self):
        await self.move_to_init()

        if self._waiting and await self.is_green_fish(*self._init_position):
            await self.to_select_click()
            await asyncio.sleep(random.expovariate(1.0 / 0.1))
            self._waiting = False
        else:
            await self.full_cicle()
            self._waiting = True

        await asyncio.sleep(0.5)
