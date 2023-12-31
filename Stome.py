import msvcrt
from Package.config import Constants
from concurrent.futures import ThreadPoolExecutor
from ClassImplementation import Info


def usage():
    print("\n`insert` to pause/resume execution,\n"
          "`escape` to break execution.\n")


def main():
    subclasses = Info().get_run_subclasses
    with ThreadPoolExecutor(max_workers=len(subclasses)) as executor, Constants() as event:
        for Class in subclasses:
            instance = Class(event.HALT, event.SHUTDOWN)
            with instance:
                executor.submit(instance.task, halt=event.HALT, shutdown=event.SHUTDOWN)
        usage()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        while msvcrt.kbhit():
            msvcrt.getch()
