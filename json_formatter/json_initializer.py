"""Format json file"""
from sys import argv
from os.path import basename, splitext
from time import sleep
from json import load, dump
from json.decoder import JSONDecodeError

def json_format(json_path: str) -> str:
    """
    Format json file.
    
    Parameters
    ----------
    json_path : str
        The path of the json file you want to format.

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

    for k in json_data.keys():
        print('key:', k)


    output_json = open(basename(json_path), "w", encoding="utf-8_sig")

    dump(json_data, output_json, ensure_ascii=False, indent=4, \
    sort_keys=True, separators=(',', ': '))

    result = "Successful!: {} was formatted.".format(basename(json_path))
    return result

def check_dict_value(target_dict: dict) -> int:
    """
    Check whether the value of dict exists or whether there are multiple values
    
    Parameters
    ----------
    target_dit : dict
        
    Returns
    ----------
    result : int
        result = 0 : Dict does not have a key
        result = 1 : Dict has only one value
        result = 2 : Dict has maltiple vakues
    """
    pass

if __name__ == "__main__":
    if len(argv) >= 2:
        for file_path in argv[1:]:
            splited = splitext(file_path)
            if splited[1] == '.json':
                result = json_format(file_path)
                print(result)
            else:
                print(basename(file_path)," is not json file")

    else:
        print("usage: Drag and drop json file to json_formatter.py")
    
    sleep(30)
