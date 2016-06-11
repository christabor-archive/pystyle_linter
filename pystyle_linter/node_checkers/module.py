"""Checker for a node Module."""

import ast

from ..errors import generic


def check(node):
    """Checker for a module."""
    report = dict(
        name='Module',
        nodetype='module',
        errors=[],
    )
    if ast.get_docstring(node) is None:
        report['errors'].append(generic.docstring(
            node,
            desc='This module has no docstring.'
        ))
    # More checks here...
    return report
