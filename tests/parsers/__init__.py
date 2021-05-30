import unittest

from .test_database import TestDatabaseParser
from .test_user import TestUserParser


def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUserParser))
    suite.addTest(unittest.makeSuite(TestDatabaseParser))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_suite())
