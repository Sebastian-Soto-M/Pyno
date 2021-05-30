PYTHON = python3
# python3
SHELL = /bin/bash

.PHONY = setup all run test-parsers test-user test clean
.DEFAULT_GOAL = test-user


setup:
	$(PYTHON) -m venv env
	@echo "Now you must source the environment just created"

all:
	@test
	@install

run:
	$(PYTHON) -m pyno

test:
	@test-parsers

test-parsers:
	$(PYTHON) -m unittest -q tests.parsers

test-user:
	$(PYTHON) -m unittest -q tests.parsers.test_user