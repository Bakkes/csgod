from csgod.handle import *
from csgod import buffer


@handles(on_server_connect)
def record_demo():
    buffer.clear()
    print("Recording")
    buffer.write("record test")
    buffer.flush()
