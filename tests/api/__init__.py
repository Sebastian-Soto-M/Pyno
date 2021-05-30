import unittest

from .test_database import TestDatabaseApi


def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDatabaseApi))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_suite())
