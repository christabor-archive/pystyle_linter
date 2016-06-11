# pystyle-linter
A proof-of-concept linter for "elements of python style" using abstract syntax trees.

**Notice** this is hardly complete -- this is not meant to be used for anything serious, but does work well with a very limited set of checkers.

## Usage

For now, it's direct access only. Eventually, I'd like to make it a package.

```shell
# Output html table.
python checker.py -f testfile.py --html foo.html
# Output json.
python checker.py -f testfile.py --jsonfile foo.json
```

## Tests

```sh
pip install py.test
cd tests
py.test -v
# Or, to view stdout
py.test -s
```
