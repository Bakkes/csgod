import winreg
from os.path import normpath as norm

import win32ui
# import win32con
# import win32api

from csgod import vdf
from csgod.exceptions import GameNotInstalledError


def game_installed():
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, norm("Software/Valve/Steam/Apps/730")) as key:
            return bool(winreg.QueryValueEx(key, 'Installed')[0])
    except OSError:
        return False


def steam_path():
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, norm("Software/Valve/Steam")) as key:
        return winreg.QueryValueEx(key, 'SteamPath')[0]


def game_path():
    if not game_installed():
        raise GameNotInstalledError

    steam_config = vdf.load(steam_path() + "/config/config.vdf")
    return steam_config[
        'InstallConfigStore'][
        'Software'][
        'Valve'][
        'Steam'][
        'apps'][
        '730'][
        'installdir'
    ].replace('\\', '/')


def game_log_path():
    if not game_installed():
        raise GameNotInstalledError

    return game_path() + "/csgo/console.log"


def game_autoexec_path():
    if not game_installed():
        raise GameNotInstalledError

    return game_path() + "/csgo/cfg/autoexec.cfg"


def game_running():
    if not game_installed():
        raise GameNotInstalledError

    try:
        win32ui.FindWindow('Valve001', 'Counter-Strike: Global Offensive')
    except win32ui.error:
        return False
    else:
        return True
