from csgod import buffer


def hook(f, pattern):
    def wrapped_hook(*args, **kargs):
        result = (f(*args, **kargs))


# class Hook:
#     def __init__(pattern):
#         pass

#     def run():
#         pass