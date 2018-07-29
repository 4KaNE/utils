"""File backuper"""
import asyncio
import datetime
from time import sleep

def save_file(file_path: str, loop) -> str:
    """Back up the specified file with rename.
       argument1: str(The path of the file you want to back up.)
       return: str(success or failed + datetime)
    """
    print(file_path)
    print(datetime.datetime.now())
    loop.call_later(3600, save_file, file_path, loop)

def check_on_the_hour() -> bool:
    """Check if the current time is on the hour.
       return: bool
    """
    now = datetime.datetime.now()
    result = True if now.minute == 0 else False
    return result

if __name__ == "__main__":
    file_path = "test/test"
    while True:
        if check_on_the_hour() is True:
            break
        else:
            print("test")
            sleep(60)

    loop = asyncio.get_event_loop()
    loop.call_soon(save_file, file_path, loop)
    loop.run_forever()