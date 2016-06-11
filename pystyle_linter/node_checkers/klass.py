"""Checker for a node ClassDef."""

import ast

from ..errors import generic


def check(node):
    """Checker for a class."""
    # ClassDef(name, bases, keywords, starargs, kwargs, body, decorator_list)
    report = dict(
        name=node.name,
        errors=[],
        nodetype='class',
    )
    # Empty bases = no object inheritance, which is considered bad.
    err_defaults = dict(
        lineno=node.lineno,
        coloffset=node.col_offset,
        nodename=node.name,
        nodetype='class',
    )
    # Check for old-style classes.
    if not node.bases:
        err = dict(
            errcode='NO_OBJECT_BASECLASS',
            desc=('This class does not inherit from `object` - '
                  'only relevant for python 2.x'),
            error_url=(
                'https://github.com/amontalenti/'
                'elements-of-python-style#always-'
                'inherit-from-object-and-use-new-style-classes'),
        )
        err.update(**err_defaults)
        report['errors'].append(err)
    # Check for exception overrides
    for base in node.bases:
        if base.id == 'Exception':
            err = dict(
                errcode='NO_CUSTOM_EXCEPTIONS',
                desc=('Try to avoid custom exceptions - the std '
                      'library is usually sufficient.')
            )
            err.update(**err_defaults)
            report['errors'].append(err)
    if ast.get_docstring(node) is None:
        err = generic.docstring(node, desc='This class has no docstring.')
        err.update(**err_defaults)
        report['errors'].append(err)
    # More checks here...
    return report
