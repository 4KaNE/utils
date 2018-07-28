"""jsonファイルを整形する"""
import sys
import os.path as path
import json

def json_format(json_path):
    file_name = json_path

    json_file = open(path.basename(file_name), 'r', encoding="utf-8_sig")
    json_data = json.load(json_file)

    output_json = open("{}".format(file_name), "w", encoding="utf-8_sig")

    json.dump(json_data, output_json, ensure_ascii=False, indent=4, \
    sort_keys=True, separators=(',', ': '))

if __name__ == "__main__":
    print(sys.argv[1])
    json_format(sys.argv[1])
    while True:
        text = input('>> ')
        print(text)