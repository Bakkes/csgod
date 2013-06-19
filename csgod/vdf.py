import re


def loads(s):
    colons_added = re.sub(r'"(?=\s*\{|[ \t]*")', r'":', s, flags=re.MULTILINE)
    commas_added = re.sub(r'(["\}])(?=$)(?!\s*(\}|\Z))', r'\1,', colons_added, flags=re.MULTILINE)
    final = "{%s}" % commas_added

    parsed = eval(final)
    return parsed


def load(file_path):
    with open(file_path, 'r') as opened:
        return loads(opened.read())
