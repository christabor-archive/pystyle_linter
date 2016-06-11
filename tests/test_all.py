"""Basic tests."""

import ast
from pprint import pprint as ppr

from pystyle_linter.checker import CheckerVisitor

# provide default with a module docstring to filter out the error.
default_code = """""\"Some docstring.""\"\n{code}"""


def _get_report(data):
    """Create an ast, visit, and return the report."""
    tree = ast.parse(data)
    checker = CheckerVisitor()
    checker.visit(tree)
    return checker.get_report()


def test_no_docstring_module():
    f = _get_report('')
    assert f[0]['errors'][0]['errcode'] == 'NO_DOCSTRING'


def test_no_docstring_func():
    code = default_code.format(code='def foo(): pass')
    f = _get_report(code)
    assert f[0]['errors'][0]['errcode'] == 'NO_DOCSTRING'


def test_override_exception():
    code = default_code.format(code='class ArgumentError(Exception): pass')
    f = _get_report(code)
    assert f[0]['errors'][0]['errcode'] == 'NO_CUSTOM_EXCEPTIONS'


def test_oldstyleclass():
    code = default_code.format(code='class JSONWriter:\n\t"""old."""')
    f = _get_report(code)
    assert f[0]['errors'][0]['errcode'] == 'NO_OBJECT_BASECLASS'


def test_no_ctxmgr():
    code = default_code.format(code='open("foo.file")')
    f = _get_report(code)
    assert f[0]['errors'][0]['errcode'] == 'USE_CTXMGR'


def test_isinstance():
    code = default_code.format(code='type(foo)')
    f = _get_report(code)
    assert f[0]['errors'][0]['errcode'] == 'USE_ISINSTANCE'


def test_use_comprehension():
    code = default_code.format(code='map(range(10), lambda x: x)')
    f = _get_report(code)
    assert f[0]['errors'][0]['errcode'] == 'USE_LISTCOMPREHENSION'
