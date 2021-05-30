import json
import logging
import time
from unittest import TestCase, main, skip

import requests
from pyno.api import NotionApi
from pyno.models import Database
from pyno.parsers import ResponseListModel
from pyno.parsers.database import parse_database
from pyno.utils import debug_json

URL = 'https://api.notion.com/v1/databases'


class TestDatabaseApi(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        self.logger.info('%s:\t%.3f' % (self.id().split('.')[-1], t))

    def test_get_all(self):
        obj = NotionApi.get_all_databases()
        debug_json(self.logger, 'Databases', obj.dict())


if __name__ == "__main__":
    main()
