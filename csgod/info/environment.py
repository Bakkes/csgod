import winreg
import os.path

import win32ui
# import win32con
# import win32api

from csgod import vdf
from csgod.exceptions import GameNotInstalledError


def game_installed():
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam\Apps\730") as key:
            return bool(winreg.QueryValueEx(key, 'Installed')[0])
    except OSError:
        return False


# Decorator
def requires_game(f):
    def run_if_installed(*args, **kargs):
        if not game_installed():
            raise GameNotInstalledError
        return f(*args, **kargs)
    return run_if_installed


def steam_path():
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam") as key:
        return winreg.QueryValueEx(key, 'SteamPath')[0]


@requires_game
def game_path():
    steam_config = vdf.load(os.path.join(steam_path(), r"config\config.vdf"))
    return steam_config['InstallConfigStore']['Software'][
            'Valve']['Steam']['apps']['730']['installdir']


@requires_game
def game_log_path():
    return os.path.join(game_path(), r"csgo\console.log")


@requires_game
def game_autoexec_path():
    return os.path.join(game_path(), r"csgo\cfg\autoexec.cfg")


@requires_game
def game_valverc_path():
    return os.path.join(game_path(), r"csgo\cfg\valve.rc")


@requires_game
def game_running():
    try:
        win32ui.FindWindow('Valve001', 'Counter-Strike: Global Offensive')
    except win32ui.error:
        return False
    else:
        return True


@requires_game
def player_name():
    with open(os.path.join(game_path(), r"csgo\cfg\config.cfg"), 'r') as config:
        for line in config:
            if line.startswith('name '):
                return line.split('"')[1]
