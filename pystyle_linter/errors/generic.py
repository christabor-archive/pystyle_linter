"""Reusable error values as functions."""


def docstring(node, nodetype=None, desc='no description', error_url=None):
    """Handle the error template for a missing docstring."""
    return dict(
        errcode='NO_DOCSTRING',
        desc=desc,
        lineno=node.lineno if hasattr(node, 'lineno') else None,
        coloffset=node.col_offset if hasattr(node, 'col_offset') else None,
        nodetype=nodetype,
        error_url=error_url,
    )
