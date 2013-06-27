import time
import os.path

import win32api
import win32con
import win32com.client
import win32ui

from csgod import info


FLUSH_KEY = 'F8'
BUFFER_FILE_NAME = 'csgodbuffer.cfg'

_SHELL = win32com.client.Dispatch('WScript.Shell')


def write(string):
    with open(os.path.join(info.environment.game_path(), r'csgo\cfg', BUFFER_FILE_NAME), 'a') as buffer:
        buffer.write(string)


def writeline(string):
    write(string + "\n")


def clear():
    with open(os.path.join(info.environment.game_path(), r'csgo\cfg', BUFFER_FILE_NAME), 'w'):
        pass


def flush(padding=1):
    # Send the flush key.
    # _SHELL.AppActivate('Counter-Strike: Global Offensive')
    # _SHELL.SendKeys('{%s}' % FLUSH_KEY, 0)
    window = win32ui.FindWindow('Valve001', 'Counter-Strike: Global Offensive')

    time.sleep(padding)
    clear()
