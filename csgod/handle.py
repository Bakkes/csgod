import time

from csgod.buffer import write, flush


def init(monitor):
    globals().update(monitor.hooks)


# Decorator
def handles(hook, before_padding=0):
    def register(handler):
        nonlocal hook
        def padded(*args, **kargs):
            time.sleep(before_padding)
            results = handler(*args, **kargs)
            return results
        hook.append(padded)
        return padded
    return register
