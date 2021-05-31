import json
import logging
import time
from unittest import TestCase, main

from pyno.api import URL, NotionApi
from pyno.parsers.database import parse_database, parse_database_list
from pyno.utils import FORMAT, debug_json
from requests import Response

user_url = f'{URL}/databases'


class TestDatabaseApi(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestDatabaseApi.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    def test_get_by_id(self):
        uid = 'ed0cac1b-641f-4a3c-9ca3-e0bf6145d216'
        obj_response: Response = NotionApi.get_database(uid)
        obj = parse_database(obj_response)
        debug_json(self.logger, 'Databases', json.loads(obj.json()))
        self.assertEqual(obj_response.status_code, 200)

    def test_get_all(self):
        obj_response: Response = NotionApi.get_all_databases()
        obj = parse_database_list(obj_response)
        debug_json(self.logger, 'Databases', json.loads(obj.json()))
        self.assertEqual(obj_response.status_code, 200)


if __name__ == "__main__":
    main()
