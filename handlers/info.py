from csgod.handle import *
from csgod import info


@handles(on_server_map_change)
def update_map(new_map):
    info.ingame.current_map = new_map
