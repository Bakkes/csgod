import time

from csgod.buffer import write, flush


def init(monitor):
    globals().update(monitor.hooks)


# Decorator
def handles(hook, before_padding=0, after_padding=0.25):
    def register(handler):
        nonlocal hook
        hook.append(handler)
        def padded(*args, **kargs):
            time.sleep(before_padding)
            results = handler(*args, **kargs)
            time.sleep(after_padding)
            return results
        return padded
    return register
