import sys
import logging

from csgod import autoexec, handle
from csgod.monitor import Monitor
from csgod.exceptions import GameNotInstalledError


def log_exception(typ, value, traceback):
    logging.critical("Exception")
    logging.critical("Type: %s" % typ)
    logging.critical("Value: %s" % value)
    logging.critical("Traceback: %s" % traceback)


def main():
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    sys.excepthook = log_exception
    with open('debug.log', 'a') as log:
        log.write('\n')

    try:
        autoexec.init()

        m = Monitor()
        handle.init(m)
        m.start()
    except KeyboardInterrupt:
        logging.info("Program manually stopped.")
    except GameNotInstalledError:
        logging.info("Game not installed.")


if __name__ == "__main__":
    main()
