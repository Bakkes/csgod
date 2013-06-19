import re

from csgod import info, buffer


INIT_FILE_NAME = 'csgodinit.cfg'
INIT_FILE_CONTENTS = '''
bind {flush_k} "exec {buffer_f}"
'''.format(
    flush_k=buffer.FLUSH_KEY,
    buffer_f=buffer.BUFFER_FILE_NAME
)


def init():
    if not initialised():
        with open(info.game_autoexec_path(), 'a') as autoexec:
            autoexec.write('\nexec "%s"\n' % INIT_FILE_NAME)
    with open(info.game_path() + '/csgo/' + INIT_FILE_NAME, 'w') as init_file:
        init_file.write(INIT_FILE_CONTENTS)


def initialised():
    pattern = re.compile(r'(^|.*;)[ \t]*exec[ \t]+("?)%s\2[ \t]*(;|$)' % INIT_FILE_NAME)
    with open(info.game_autoexec_path(), 'r') as autoexec:
        for line in autoexec:
            if pattern.match(line):
                return True
    return False
