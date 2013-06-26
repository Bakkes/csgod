import sys
import logging

from csgod import autoexec, handle
from csgod.monitor import Monitor
from csgod.exceptions import GameNotInstalledError


def main():
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    # sys.excepthook = log_exception
    with open('debug.log', 'a') as log:
        log.write('\n')

    try:
        autoexec.init()

        m = Monitor()
        m.start()
    except KeyboardInterrupt:
        logging.info("Program manually stopped.")
    except GameNotInstalledError:
        logging.info("Game not installed.")
    except Exception as e:
        logging.exception("Unhandled exception.")
        raise


if __name__ == "__main__":
    main()
