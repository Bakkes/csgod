import time
import re

from csgod import info


class Monitor:
    """Monitors a CS:GO process and notifies listeners when events occur."""

    def __init__(self, runcheck_interval=5):
        self.runcheck_interval = runcheck_interval
        self.running = False

        self.log = open(info.game_log_path(), 'r')
        self.hooks = {}
        # pattern_hooks = {re.compile(pattern): func for (pattern, func) in {
        #     r'pattern': func
        # }.items()}

    def clear_log():
        with open(info.game_log_path(), 'w'):
            pass

    def start(self):
        self.running = True
        self.run()

    def stop(self):
        self.running = False
        self.log.close()

    def run(self):
        while self.running:
            clear_log()
            self.log.seek(0)

            while info.game_running():
                pos = self.log.tell()
                line = self.log.readline()
                if line:
                    self.process_line(line.rstrip())
                elif line is '\n':
                    continue
                else:
                    # print(".", end='')
                    # sys.stdout.flush()
                    self.log.seek(pos)
                    time.sleep(1)

            # Wait before checking whether game is running again.
            time.sleep(self.runcheck_interval)

    def process_line(self, line):
        # Match each regex on the string
        matches = (
            (pattern.match(line), f) for pattern, f in self.hooks
        )

        # Filter out empty matches, and extract groups
        matches = (
            (match.groups(), f) for match, f in matches if match and f
        )

        # Delegate to the functions
        for args, f in matches:
            f(*args)

    def __getitem__(self, key):
        return self.hooks[re.compile(key)]

    def __setitem__(self, key, value):
        self.hooks[re.compile(key)] = value

    def __delitem__(self, key):
        del self.hooks[re.compile(key)]
