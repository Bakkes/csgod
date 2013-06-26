import time
import os.path

import win32com
import win32com.client

from csgod import info


FLUSH_KEY = 'F8'
BUFFER_FILE_NAME = 'csgodbuffer.cfg'

FLUSH_SLEEP_TIME = 0.25

_SHELL = win32com.client.Dispatch('WScript.Shell')


def write(string):
    with open(os.path.join(info.environment.game_path(), r'csgo\cfg', BUFFER_FILE_NAME), 'a') as buffer:
        buffer.write(string)


def clear():
    with open(os.path.join(info.environment.game_path(), r'csgo\cfg', BUFFER_FILE_NAME), 'w'):
        pass


def flush():
    # Send the flush key.
    _SHELL.SendKeys('{%s}' % FLUSH_KEY, 0)
    time.sleep(FLUSH_SLEEP_TIME)
    clear()
