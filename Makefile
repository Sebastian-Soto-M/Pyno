PYTHON = python3
# python3
SHELL = /bin/bash

.PHONY = setup all run test-api test-parsers test-database test-user test clean
.DEFAULT_GOAL = run


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

test-api:
	$(PYTHON) -m unittest -q tests.api

test-parsers:
	$(PYTHON) -m unittest -q tests.parsers

test-database:
	$(PYTHON) -m unittest -q tests.parsers.test_database

test-user:
	$(PYTHON) -m unittest -q tests.parsers.test_user