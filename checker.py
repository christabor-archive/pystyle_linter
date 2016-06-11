"""A code linter for elements of python style.

See https://github.com/amontalenti/elements-of-python-style for more.
"""

from __future__ import absolute_import

import ast
import json

import click

from jinja2 import (
    Environment,
    PackageLoader,
)

from node_checkers import (
    call,
    func,
    klass,
    module,
)


class CheckerVisitor(ast.NodeVisitor):
    """A node visitor class that checks all node types and adds a report."""

    def __init__(self, *args, **kwargs):
        """Call parent, but add report to the class."""
        super(CheckerVisitor, self).__init__(*args, **kwargs)
        self.report = []

    def get_report(self):
        """Get the report from visiting the nodes and checking for errors."""
        return self.report

    def generic_visit(self, node):
        """Useful for debugging."""
        # print(node)
        super(CheckerVisitor, self).generic_visit(node)

    def visit_Call(self, node):
        """Handle function call."""
        # func, args, keywords, starargs, kwargs
        self.report.append(call.check(node))
        self.generic_visit(node)

    def visit_Module(self, node):
        """Handle the module."""
        self.report.append(module.check(node))
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """Handle classes."""
        self.report.append(klass.check(node))
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        """Handle functions."""
        self.report.append(func.check(node))
        self.generic_visit(node)


@click.command()
@click.option('--filename', '-f', default=None, help='A file to parse.')
@click.option('--jsonfile', '-j', default=None, help='Output results to json.')
@click.option('--html', '-h', default=None, help='Output results to html.')
def parsefile(filename, jsonfile, html):
    """Parse a single file and check for pystyle violations."""
    with open(filename, 'r+') as pyfile:
        tree = ast.parse(pyfile.read())
        checker = CheckerVisitor()
        checker.visit(tree)
        report = checker.get_report()

    if jsonfile is not None:
        with open(jsonfile, 'w+') as reportfile:
            reportfile.write(json.dumps(report, indent=4))
    if html is not None:
        env = Environment(
            loader=PackageLoader(__name__),
            trim_blocks=True,
            lstrip_blocks=True)
        with open(html, 'w+') as htmlfile:
            htmlfile.write(env.get_template('main.html').render(
                dict(
                    errcount=sum(len(item['errors']) for item in report),
                    filename=filename,
                    report=report,
                )
            ))
    if jsonfile is None and html is None:
        print('Results = ', report)


if __name__ == '__main__':
    parsefile()
