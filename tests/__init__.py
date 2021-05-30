import json
import logging
import sys
import unittest

from .parsers.test_user import TestUserParser

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout,
                    format='%(levelname)s\t| %(name)s: %(message)s')


def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUserParser))
    return suite


def run_suite():
    runner = unittest.TextTestRunner()
    runner.run(get_suite())


if __name__ == '__main__':
    run_suite()
