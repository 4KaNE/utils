"""File backuper"""
import asyncio
import datetime
import math
from time import sleep

def save_file(file_path: str, loop) -> str:
    """
    Back up the specified file with rename.
    
    Parameters
    ----------
    file_path : str
        The path of the file you want to back up.
        
    Returns
    ----------
    result : str
        success or failed + datetime
    """
    print(file_path)
    print(datetime.datetime.now())
    loop.call_later(3600, save_file, file_path, loop)

def wait_the_time() -> None:
    """
    Wait for the hour.
    """
    while True:
        now = datetime.datetime.now()
        if now.minute == 0:
            break
        else:
            diff = (3600 - (now.minute * 60 + now.second))
            interval = math.ceil(diff/2)
            print(interval)
            sleep(interval)
        
    return


if __name__ == "__main__":
    file_path = "test/test"
    wait_the_time()

    loop = asyncio.get_event_loop()
    loop.call_soon(save_file, file_path, loop)
    loop.run_forever()
