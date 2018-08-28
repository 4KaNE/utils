import os
from datetime import datetime as dt
from time import sleep
 
def create_files(dir, file_name, now_dir="."):
    now_dir = ("{}/{}".format(now_dir, file_name))
    os.mkdir(now_dir)
    for f in os.listdir(dir):
        full_name = dir + "/" + f
        if os.path.isfile(full_name):
            print(full_name)
            with open(now_dir+"/"+f, mode="w"):
                pass
        elif os.path.isdir(full_name):
            create_files(full_name+"/", f, now_dir)

if __name__ == '__main__':
    DIR = "The path of your directory"
    FILE_NAME = dt.strftime(dt.now(), "%Y_%m_%d_%H_%M_%S")
    create_files(DIR, FILE_NAME)
    sleep(60)