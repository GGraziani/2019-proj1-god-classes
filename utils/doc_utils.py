from utils.misc import *
from utils.string_utils import *

DOCSTRING = '''
2019-proj1-god-classes
by Gustavo Graziani

Commands:
{find_god_classes}
{extract_feature_vectors}

TO SEE DETAILS ON EACH COMMAND, RUN
> python3 god_classes.py <command>
'''

MODULE_DOCSTRINGS = {
    'find_god_classes': '''
find_god_classes:
    Given a source code, computes and returns a list of god classes.
 
    $ python3 god_classes find_god_classes [-s/--source] <path-to-src>
''',

    'extract_feature_vectors': '''
extract_feature_vectors:
      For each god class found on the given source code, it computes and writes to csv the respective feature vector.

    $ python3 god_classes extract_feature_vectors [-s/--source] <path-to-src>
'''
}


def docstring_preview(text):
    return text.split('\n\n')[0]


docstring_headers = {
    key: indent(docstring_preview(value))
    for (key, value) in MODULE_DOCSTRINGS.items()
}


DOCSTRING = DOCSTRING.format(**docstring_headers)



