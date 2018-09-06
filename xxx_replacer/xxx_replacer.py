"""replacer"""
from time import sleep

print('置換する元の文字列')
TARGET_STR = input('>> ')
print('置換したい文字')
REPLACE_CHARA = input('>> ')
NUM_OF_CHARA = len(TARGET_STR)
print(REPLACE_CHARA * NUM_OF_CHARA)
sleep(300)