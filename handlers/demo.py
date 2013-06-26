from csgod.handle import *

@handles(on_server_connect)
def say_hello():
    print("Hello")
