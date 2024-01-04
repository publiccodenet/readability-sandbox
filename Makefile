# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2024 The Foundation for Public Code <info@publiccode.net>

SHELL:=/bin/bash

MARKDOWN_DIR ?= "../Standard/criteria"

default: run

venv/bin/activate: requirements.txt
	rm -rf venv
	python3 -m venv venv
	source venv/bin/activate && \
	 pip3 install --upgrade pip
	source venv/bin/activate && \
	 pip3 install -r requirements.txt

.PHONY: $(MARKDOWN_DIR)
$(MARKDOWN_DIR):
	@if ! [ -e "$(MARKDOWN_DIR)" ]; then \
		echo ""; \
		echo "MARKDOWN_DIR environment variable not correct"; \
		echo ""; \
		echo "e.g.:"; \
		echo "MARKDOWN_DIR='../Standard/criteria' make"; \
		echo ""; \
		false; \
	fi

.PHONY: run
run: venv/bin/activate markdown-readability.py $(MARKDOWN_DIR)
	source venv/bin/activate && \
	 python3 ./markdown-readability.py $(MARKDOWN_DIR)

.PHONY: clean
clean:
	rm -rf venv
