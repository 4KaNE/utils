"""File backuper"""
from datetime.datetime import now, strptime
from math import ceil
from time import sleep
from os import mkdir
from os.path import isdir, basename, splitext

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
    file_data = read_file(file_path)
    if file_path is None:
        result = "failed"
        return result

    splited = os.path.splitext(os.path.basename(file_path))
    dir_path = "./{}".format(splited[0])
    if not isdir(dir_path):
        #保存用ディレクトリがない
        mkdir(dir_path)

    save_time = strptime(now(), '%Y-%m-%d %H:%M')
    save_file_path = "{}/{}{}{}".format(dirpath, splited[0], save_time, splited[1])
    
    with open(save_file_path, 'w', encoding="utf-8_sig") as save_file:
        save_file.write(file_data)
        
    result = "Success"
    return result

def read_file(file_path):
    """
    Open the file and return the contents
    
    Parameters
    ----------
    file_path : str
        The path of the file.
    
    Returns
    ----------
    file_data : str
        Data in the file
    """
    try:
        with open(file_path, 'r', encoding="utf-8_sig") as target_file:
            file_data = load(target_file)
    except FileNotFoundError:
        file_data = None
        print('File not Found!')

    return file_data

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
