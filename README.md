<!-- SPDX-License-Identifier: CC0-1.0 -->
<!-- SPDX-FileCopyrightText: 2024 The Foundation for Public Code <info@publiccode.net> -->

# readability-sandbox

An initial prototype of readability scoring of text in jekyll markdown files.

## Usage:

The system must have `make`, `python3`, and `python3-venv` installed.

The `Makefile` expects to be called with the environment variable `MARKDOWN_DIR` set to a location with jekyll markdown files:

```Shell
make MARKDOWN_DIR='path/to/directory'
```

## LICENSE

The software is [licensed](LICENSE) under CC 0.
This means anyone can do anything with it.
If you contribute to this repository, you also grant these rights to others.
