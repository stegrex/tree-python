# tree-python

Python-based command-line utility for recursively listing directories and files
inspired by, but not emulating Steve Baker's tree for Linux.

## Setup

This currently supports Python 3 only.

Before use, make sure to run the following in command line (valid for the
current terminal session only):

```
$ alias tree-python="sudo python3 /path/to/tree-python/tree-python.py"
```

Where `tree-python` stands for the command you want to use, and `python3` is
the command for your Python interpreter. Note that Python 3 must be installed.

## Usage

```
$ tree-python
```

or:

```
$ python3 /path/to/tree-python/tree-python.py
```