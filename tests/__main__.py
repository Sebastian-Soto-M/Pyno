import unittest

from .api import TESTS as API_TESTS
from .parsers import TESTS as PARSER_TESTS

TESTS = API_TESTS.union(PARSER_TESTS)


def get_suite():
    suite = unittest.TestSuite()
    for test in TESTS:
        suite.addTest(unittest.makeSuite(test))
    return suite


def run_suite():
    runner = unittest.TextTestRunner()
    runner.run(get_suite())


if __name__ == '__main__':
    run_suite()
