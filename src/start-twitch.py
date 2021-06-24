import os
import time

import sys
args = sys.argv

username = 'therealkebom'
password = '539cau4d49cvwlzrdc2x4kjieg47mh'
channel_name = 'therealkebom'
msg = args[1]

def start():
    try:
        os.system(f'node src/src/bot.js {username} {password} {channel_name} {msg}')
    except Exception as e:
        print(e)

start()