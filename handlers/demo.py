from csgod.handle import *
from csgod import buffer
import time

@handles(on_server_connect)
def record_demo():
    print("lol")
    buffer.clear()
    time.sleep(3)
    buffer.write("say tits")
    buffer.flush()
