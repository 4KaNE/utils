"""File backuper"""
from datetime.datetime import now, strptime
from math import ceil
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
        success or failed
    """

    return "Success or Failed"

def wait_the_time() -> str:
    """
    Wait for the hour.
    
    Returns
    ----------
    date_str : str
        Time to start processing
    """
    while True:
        now = now()
        if now.minute == 0:
            break
        else:
            diff = (3600 - (now.minute * 60 + now.second))
            interval = ceil(diff/2)
            print(interval)
            sleep(interval)

        now_str = strptime(now, '%Y-%m-%d %H:%M:%S')
        
    return now_str


if __name__ == "__main__":
    file_path = "test/test"
    while True:
        print(wait_the_time())
        print(save_file(file_path))
