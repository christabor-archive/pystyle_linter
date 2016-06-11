"""Checker for a function call."""


def check(node):
    """Check the node for errors."""
    report = dict(
        name=node.name if hasattr(node, 'name') else 'noname',
        nodetype='call',
        errors=[],
    )
    err_default = dict(
        lineno=node.lineno,
        coloffset=node.col_offset,
    )
    # Stop if there is not id.
    if not hasattr(node.func, 'id'):
        return report
    if node.func.id == 'type':
        err = dict(
            desc='Consider using `isinstance` instead of `type`.',
            errcode='USE_ISINSTANCE',
        )
        err.update(**err_default)
        report['errors'].append(err)
    if node.func.id == 'open':
        err = dict(
            desc=('This function uses `open`. '
                  'Use the `with` context manager instead.'),
            errcode='USE_CTXMGR',
        )
        err.update(**err_default)
        report['errors'].append(err)
    if node.func.id == 'map':
        err = dict(
            desc=('This function uses `map`. Consider using a '
                  'comprehension instead, if it makes sense.'),
            errcode='USE_LISTCOMPREHENSION',
        )
        err.update(**err_default)
        report['errors'].append(err)
    return report
