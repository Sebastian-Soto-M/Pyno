PYTHON = python3
# python3
SHELL = /bin/bash

.PHONY:
	all
	clean
	run
	setup

	test

	test-api
	test-database-api
	test-user-api

	test-parsers
	test-database-parser
	test-user-parser

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
	$(PYTHON) -m tests

test-api:
	$(PYTHON) -m unittest -q tests.api

test-database-api:
	$(PYTHON) -m unittest -q tests.api.test_database

test-user-api:
	$(PYTHON) -m unittest -q tests.api.test_user

test-parsers:
	$(PYTHON) -m unittest -q tests.parsers

test-database-parser:
	$(PYTHON) -m unittest -q tests.parsers.test_database

test-user-parser:
	$(PYTHON) -m unittest -q tests.parsers.test_user