import logging
import time
from unittest import TestCase, main, skip

import requests
import responses
from pyno.models import Bot, Person, UserTypeEnum
from pyno.parsers import ResponseListModel
from pyno.parsers.user import parse_user, parse_user_list
from pyno.utils import FORMAT, debug_json

URL = 'https://api.notion.com/v1/users'

RESPONSE_BODIES = {
    'get_person': {"id": "848e2e82-bc8c-498b-8e84-396d73a11229", "type": "person", "person": {"email": "ssotom@ucenfotec.ac.cr"}, "name": "Sebastian Soto",
                   "avatar_url": "https://lh3.googleusercontent.com/a-/AOh14GhIhEIdpo59riYv1q3NgiCRDVccZBUwNEWSMRG9gg=s100", "object": "user"},
    'get_bot': {"id": "848e2e82-bc8c-498b-8e84-396d73a11229", "type": "bot", "bot": {}, "name": "JIJI Bot",
                "avatar_url": "https://lh3.googleusercontent.com/a-/AOh14GhIhEIdpo59riYv1q3NgiCRDVccZBUwNEWSMRG9gg=s100", "object": "user"},
    'get_all_users': {"results": [{"object": "user", "id": "848e2e82-bc8c-498b-8e84-396d73a11229", "name": "Sebastian Soto", "avatar_url": "https://lh3.googleusercontent.com/a-/AOh14GhIhEIdpo59riYv1q3NgiCRDVccZBUwNEWSMRG9gg=s100", "type": "person", "person": {"email": "ssotom@ucenfotec.ac.cr"}}, {"object": "user", "id": "edf815fa-cbd2-4b99-bb10-b598d4026d30", "name": "DemoSandbox", "avatar_url": None, "type": "bot", "bot": {}}], "next_cursor": None, "object": "list", "has_more": False}
}


class TestUserParser(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestUserParser.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    @responses.activate
    def test_person(self):
        body = RESPONSE_BODIES['get_person']
        uid = body['id']
        endpoint = f'{URL}/{uid}'

        responses.add(responses.GET, endpoint, json=body, status=200)
        obj = parse_user(requests.get(endpoint))
        debug_json(self.logger, 'Person', obj.dict())
        self.assertIsInstance(obj, Person)

    @responses.activate
    def test_bot(self):
        body = RESPONSE_BODIES['get_bot']
        uid = body['id']
        endpoint = f'{URL}/{uid}'

        responses.add(responses.GET, endpoint, json=body, status=200)
        obj = parse_user(requests.get(endpoint))
        debug_json(self.logger, 'Bot', obj.dict())
        self.assertIsInstance(obj, Bot)

    @responses.activate
    def test_user_type_enum(self):
        body = RESPONSE_BODIES['get_bot']
        uid = body['id']
        endpoint = f'{URL}/{uid}'

        responses.add(responses.GET, endpoint, json=body, status=200)
        obj = parse_user(requests.get(endpoint))
        self.assertEqual(obj.type, UserTypeEnum.BOT)

    @responses.activate
    def test_list(self):
        body = RESPONSE_BODIES['get_all_users']
        endpoint = URL

        responses.add(responses.GET, endpoint, json=body, status=200)
        res = requests.get(endpoint)
        ul = parse_user_list(res)
        debug_json(self.logger, 'User List', ul.dict())
        self.assertIsInstance(ul, ResponseListModel)


if __name__ == "__main__":
    main()
