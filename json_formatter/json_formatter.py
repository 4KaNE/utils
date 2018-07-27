"""jsonファイルを整形する"""
import json

FILE_NAME = input('>> ')

FILE = open("{}.json".format(FILE_NAME), 'r', encoding="utf-8_sig")
JSON_DATA = json.load(FILE)

OUTPUT_JSON = open("{}.json".format(FILE_NAME), "w", encoding="utf-8_sig")

json.dump(JSON_DATA, OUTPUT_JSON, ensure_ascii=False, indent=4, \
sort_keys=True, separators=(',', ': '))
