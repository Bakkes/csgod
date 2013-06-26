import os
import time
import re
import json
import logging
import importlib

from csgod import info, handle
from csgod.exceptions import InvalidHookFileError


class Hook(list):
    """An event hook, containing a list of listeners to call when the hook is triggered.
    """

    def __init__(self, pattern):
        super().__init__()
        self.pattern = pattern

    def lines(self):
        return len(self.pattern)

    def __call__(self, *args, **kargs):
        for listener in self:
            listener(*args, **kargs)

    def __repr__(self):
        return "Hook(handlers%s)" % super().__repr__()


class Monitor:
    """Monitors a CS:GO process and notifies listeners when events occur.
    """

    def __init__(self, runcheck_interval=5, logcheck_interval=1):
        self.runcheck_interval = runcheck_interval
        self.logcheck_interval = logcheck_interval
        self.running = False

        # self.log = open(info.environment.game_log_path(), 'r')

        self.hooks = {}
        self.load_hooks()
        self.sorted_hooks = sorted(self.hooks.values(), key=lambda hook: hook.lines())

        handle.init(self)
        self.handlers = []
        self.load_handlers()

        print(str(self.hooks))
        print(str(self.handlers))

    def load_hooks(self):
        valid_ident_pattern = re.compile(r'[_A-Za-z][_a-zA-Z0-9]*$')
        env_vars = {
            'player': info.environment.player_name()
        }

        files = (entry for entry in os.listdir("hooks")
            if os.path.isfile(os.path.join("hooks", entry))
        )
        for file_name in files:
            # Try to read as json hook definition file.
            try:
                with open(os.path.join("hooks", file_name), 'r') as hook_file:
                    content = json.load(hook_file)
                    # TODO: Validate
                    for local_name, pattern_set in content.items():
                        # Create python-style hook name.
                        name_parts = [part.replace(" ", "_") for part in
                            ('on', file_name.split('.')[0], local_name)
                        ]
                        name = '_'.join(name_parts).lower()
                        if not valid_ident_pattern.match(name):
                            raise ValueError("Invalid identifier: " + name)

                        # Substitute variables into pattern and compile.
                        pattern = [re.compile(line.format(**env_vars)) for line in pattern_set]

                        # Register the hook.
                        self.hooks[name] = Hook(pattern)
            except (KeyError, ValueError) as error:
                logging.error(file_name + " is not a valid hook file. It has been ignored.")
                if str(error):
                    logging.error(str(error))

    def load_handlers(self):
        modules = [entry.split('.')[0] for entry in os.listdir("handlers")]
        loaders = {module: importlib.find_loader(module, ["handlers"]) for module in modules}
        self.handlers = [loader.load_module(name) for name, loader in loaders.items() if loader]
        # Now go and read http://en.wikipedia.org/wiki/Semantic_satiation

    def clear_log(self):
        with open(info.environment.game_log_path(), 'w'):
            pass

    def get_line(self):
        pos = self.log.tell()
        line = self.log.readline()
        if line:
            return(line.rstrip())
        else:
            self.log.seek(pos)
            time.sleep(self.logcheck_interval)
            return None

    def start(self):
        self.running = True
        self.clear_log()
        # self.log = open(self.log.name, self.log.mode)
        self.log = open(info.environment.game_log_path(), 'r')
        self.run()

    def stop(self):
        self.running = False
        self.log.close()

    def run(self):
        print("Looking for game process")
        while self.running:
            print("...trying again in %s seconds" % str(self.runcheck_interval))
            while info.environment.game_running():
                self.process_line()

            # Wait before checking whether game is running again.
            time.sleep(self.runcheck_interval)

    def process_line(self):
        before = self.log.tell()
        line = self.get_line()
        after = self.log.tell()
        # print("P" + str(before))
        # If the line is not empty or EOF.
        if line:
            # Match the line against each pattern in the hook dictionary.
            for hook in self.sorted_hooks:
                self.log.seek(before)
                line = self.get_line()
                # Gather the information to pass to the hook handlers.
                groups = []
                for sub_pattern in hook.pattern:
                    match = sub_pattern.match(line)
                    if match:
                        groups.extend(match.groups())
                        # Wait for a valid line of input
                        while not line:
                            line = self.get_line()
                    else:
                        # If one of the lines doesn't match the pattern, stop matching the hook.
                        break
                else:
                    # Dispatch to the hook handlers.
                    print("EVENT")
                    logging.info("An event has been triggered.")
                    hook(*groups)
                    continue
                # If one of the sub-patterns didn't match, break from this hook.
                break
        self.log.seek(after)


    def __getattr__(self, attr):
        return self.hooks[attr]

    # def __setattr__(self, attr, val):
    #     self.hooks[attr] = val

    # def __getitem__(self, key):
    #     return self.hooks[re.compile(key)]

    # def __setitem__(self, key, value):
    #     self.hooks[re.compile(key)] = value

    # def __delitem__(self, key):
    #     del self.hooks[re.compile(key)]
