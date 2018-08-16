"""Compress json file"""
from sys import argv
from os.path import basename, splitext
from time import sleep
from json import load, dump
from json.decoder import JSONDecodeError

def json_compress(json_path: str) -> str:
    """
    Compress json file.
    
    Parameters
    ----------
    json_path : str
        The path of the json file you want to compress.

    Return
    ----------
    result : str
        success or failed.
    """
    try:
        with open(json_path, 'r', encoding="utf-8_sig") as json_file:
            json_data = load(json_file)
    except JSONDecodeError:
        result = "Failed...: JSONDecodeError occurred in {}"\
        .format(basename(json_path))
        return result

    output_json = open(basename(json_path), "w", encoding="utf-8_sig")

    dump(json_data, output_json, ensure_ascii=False, separators=(',', ':'))

    result = "Successful!: {} was compressed.".format(basename(json_path))
    return result

if __name__ == "__main__":
    if len(argv) >= 2:
        for file_path in argv[1:]:
            splited = splitext(file_path)
            if splited[1] == '.json':
                result = json_compress(file_path)
                print(result)
            else:
                print(basename(file_path)," is not json file")

    else:
        print("usage: Drag and drop json file to json_compresser.py")
    
    sleep(30)
