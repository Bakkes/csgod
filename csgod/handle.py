def init(monitor):
    globals().update(monitor.hooks)


# Decorator
def handles(hook):
    def wrap(handler):
        nonlocal hook
        hook.append(handler)
        return handler
    return wrap
