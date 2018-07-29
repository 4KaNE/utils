"""File backuper"""
import asyncio
import datetime

def save_file(file_path: str, loop) -> str:
    """Back up the specified file with rename.
       argument1: str(The path of the file you want to back up.)
       return: str(success or failed + datetime)
    """
    print(file_path)
    print(datetime.datetime.now())
    loop.call_later(10, save_file, file_path, loop)

if __name__ == "__main__":
    file_path = "test/test"
    loop = asyncio.get_event_loop()
    loop.call_soon(save_file, file_path, loop)
    loop.run_forever()