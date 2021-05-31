import unittest

from .test_database import TestDatabaseParser
from .test_user import TestUserParser

TESTS = {TestUserParser, TestDatabaseParser}


def get_suite():
    suite = unittest.TestSuite()
    suite.addTests(TESTS)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_suite())
