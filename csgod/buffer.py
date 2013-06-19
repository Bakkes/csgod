import win32com
import win32com.client

from csgod import info


FLUSH_KEY = 'F8'
BUFFER_FILE_NAME = 'csgodbuffer.cfg'

_SHELL = win32com.client.Dispatch('WScript.Shell')


def write(string):
    with open(info.game_path() + '/csgo/' + BUFFER_FILE_NAME, 'a') as buffer:
        buffer.write(string)


def clear():
    with open(info.game_path() + '/csgo/' + BUFFER_FILE_NAME, 'w'):
        pass


def flush():
    # Send the flush key.
    _SHELL.SendKeys('{%w}' % FLUSH_KEY, 0)
    clear()
