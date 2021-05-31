import json
import logging
import time
from unittest import TestCase, main, skip

from pyno.api import URL, NotionApi
from pyno.parsers.database import parse_database
from pyno.parsers.user import parse_user, parse_user_list
from pyno.utils import FORMAT, debug_json

user_url = f'{URL}/users'


class TestUserApi(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestUserApi.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    def test_get_by_id(self):
        uid = "848e2e82-bc8c-498b-8e84-396d73a11229"
        obj = parse_user(NotionApi.get_user(uid))
        debug_json(self.logger, 'Users', obj.dict())

    def test_get_all(self):
        obj = parse_user_list(NotionApi.get_all_users())
        debug_json(self.logger, 'Users', obj.dict())


if __name__ == "__main__":
    main()
