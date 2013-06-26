from csgod.handle import *
from csgod import buffer


@handles(on_server_connect)
def record_demo():
    buffer.write("say tits")
    buffer.flush()
