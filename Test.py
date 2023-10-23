from Stome import Run
import asyncio
import msvcrt
import keyboard


class Test1(Run):

    async def task(self, event):
        while True:
            await self.return_value(event)
            await event.wait()


class Test2(Run):

    async def task(self, event):
        while True:
            await self.return_value(event)
            await event.wait()


class Key(Run):

    async def task(self, event):
        while True:
            is_pressed = keyboard.is_pressed(hotkey="insert")
            if is_pressed and not _was_pressed:
                event.clear() if event.is_set() else event.set()
                print("Switch state:", event.is_set())

            _was_pressed = is_pressed
            await asyncio.sleep(0.1)


async def main():
    halt = asyncio.Event()
    subclasses = [globals()[index.__name__] for index in Run.__subclasses__()]

    async with asyncio.TaskGroup() as group:
        for Class in subclasses:
            instance = Class(halt)
            async with instance:
                group.create_task(instance.task(halt))


try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
finally:
    while msvcrt.kbhit():
        msvcrt.getch()
