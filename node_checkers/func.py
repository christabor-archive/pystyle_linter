"""Checker for a node FunctionDef."""

import ast

from errors import generic


def check(node):
    """Checker for a function."""
    report = dict(name=node.name, errors=[])
    # No docstrings.
    if ast.get_docstring(node) is None:
        report['errors'].append(generic.docstring(
            node,
            nodetype='func',
            desc='This function has no docstring.'
        ))
    return report
