import unittest

from .test_database import TestDatabaseApi
from .test_user import TestUserApi

TESTS = {TestDatabaseApi, TestUserApi}


def get_suite():
    suite = unittest.TestSuite()
    suite.addTests(TESTS)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_suite())
