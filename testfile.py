import sys

#
# -----------------------------------------------
#

from itertools import groupby, chain, \
                      izip, islice


# good
from itertools import (groupby, chain,
                       izip, islice)


# -----------------------------------------------


sys.path.insert(0, '.../')


# -----------------------------------------------


class ArgumentError(Exception):
    pass


# -----------------------------------------------

open('foo')

# -----------------------------------------------


type('foo')


# -----------------------------------------------


# bad

class JSONWriter:
    """old."""

# good

class NewJSONWriter(object):
    """new."""

# -----------------------------------------------

class NoDocString:
    pass

# -----------------------------------------------

def foo(*args, **kwargs):
    pass

# -----------------------------------------------

def truncate(string):
    return string[1:]

# bad
map(truncate, filter(lambda x: len(x) > 30, items))

# good
[truncate(x) for x in ['foo', 'bar', 'asdasdsadasdasda'] if len(x) > 30]


# -----------------------------------------------
#
