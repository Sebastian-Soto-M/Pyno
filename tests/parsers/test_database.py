import json
import logging
import time
from unittest import TestCase, main, skip

import requests
import responses
from pyno.api import URL
from pyno.models import DatabaseModel
from pyno.parsers import ResponseListModel
from pyno.parsers.database import parse_database, parse_database_list
from pyno.utils import FORMAT, debug_json

user_url = f'{URL}/databases'

RESPONSE_BODIES = {
    'get_database': {
        "object": "database",
        "id": "ed0cac1b-641f-4a3c-9ca3-e0bf6145d216",
        "created_time": "2021-05-29T16:59:56.961Z",
        "last_edited_time": "2021-05-29T17:03:00.000Z",
        "title": [
            {
                "type": "text",
                "text": {
                        "content": "Test",
                        "link": None
                },
                "annotations": {
                    "bold": False,
                    "italic": False,
                    "strikethrough": False,
                    "underline": False,
                    "code": False,
                    "color": "default"
                },
                "plain_text": "Test",
                "href": None
            }
        ],
        "properties": {
            "Food group": {
                "id": "SAn`",
                "type": "select",
                "select": {
                        "options": []
                }
            },
            "Description": {
                "id": "X[S_",
                "type": "rich_text",
                "rich_text": {}
            },
            "Price": {
                "id": "~WW<",
                "type": "number",
                "number": {
                        "format": "number"
                }
            },
            "Name": {
                "id": "title",
                "type": "title",
                "title": {}
            }
        }
    },
    'get_all_databases': {"results": [
        {
            "object": "database",
            "id": "5f7f1bcd-fff0-4414-ac5c-d7099b871726",
            "created_time": "2021-05-21T02:24:08.590Z",
            "last_edited_time": "2021-05-30T18:31:00.000Z",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Demo",
                        "link": None
                    },
                    "annotations": {
                        "bold": False,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                        "code": False,
                        "color": "default"
                    },
                    "plain_text": "Demo",
                    "href": None
                }
            ],
            "properties": {
                "fd": {
                    "id": "Banj",
                    "type": "rich_text",
                    "rich_text": {}
                },
                "rank": {
                    "id": "G{I=",
                    "type": "select",
                    "select": {
                        "options": [
                            {
                                "id": "1b6ad290-f86c-459b-a6c6-9985c73b0b72",
                                "name": "1",
                                "color": "purple"
                            },
                            {
                                "id": "10bfe93a-5d4b-4a78-a55a-7209e3753e73",
                                "name": "2",
                                "color": "yellow"
                            }
                        ]
                    }
                },
                "game_type": {
                    "id": "KPR^",
                    "type": "multi_select",
                    "multi_select": {
                        "options": [
                            {
                                "id": "824c222c-6f9c-48e0-88fe-b54ded06320a",
                                "name": "test",
                                "color": "red"
                            },
                            {
                                "id": "b5f30386-55e0-42f9-9de1-823639102aca",
                                "name": "ts",
                                "color": "yellow"
                            },
                            {
                                "id": "d1459816-1814-48fc-ae77-f891834cb8ce",
                                "name": "hi",
                                "color": "green"
                            }
                        ]
                    }
                },
                "Column 2": {
                    "id": "RR]p",
                    "type": "number",
                    "number": {
                        "format": "percent"
                    }
                },
                "Column 3": {
                    "id": "SP~H",
                    "type": "files",
                    "files": {}
                },
                "Column": {
                    "id": "[h<J",
                    "type": "date",
                    "date": {}
                },
                "Column 1": {
                    "id": "jE@v",
                    "type": "url",
                    "url": {}
                },
                "creation_date": {
                    "id": "l>fs",
                    "type": "created_time",
                    "created_time": {}
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": {}
                }
            }
        },
        {
            "object": "database",
            "id": "46c95b67-9cc1-4cbf-89c0-9cdd54e16fff",
            "created_time": "2021-05-28T06:08:44.087Z",
            "last_edited_time": "2021-05-28T06:10:00.000Z",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Prueba",
                        "link": None
                    },
                    "annotations": {
                        "bold": False,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                        "code": False,
                        "color": "default"
                    },
                    "plain_text": "Prueba",
                    "href": None
                }
            ],
            "properties": {
                "Tags": {
                    "id": "Ar|x",
                    "type": "multi_select",
                    "multi_select": {
                        "options": []
                    }
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": {}
                }
            }
        },
        {
            "object": "database",
            "id": "ed0cac1b-641f-4a3c-9ca3-e0bf6145d216",
            "created_time": "2021-05-29T16:59:56.961Z",
            "last_edited_time": "2021-05-29T17:03:00.000Z",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Test",
                        "link": None
                    },
                    "annotations": {
                        "bold": False,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                        "code": False,
                        "color": "default"
                    },
                    "plain_text": "Test",
                    "href": None
                }
            ],
            "properties": {
                "Food group": {
                    "id": "SAn`",
                    "type": "select",
                    "select": {
                        "options": []
                    }
                },
                "Description": {
                    "id": "X[S_",
                    "type": "rich_text",
                    "rich_text": {}
                },
                "Price": {
                    "id": "~WW<",
                    "type": "number",
                    "number": {
                        "format": "number"
                    }
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": {}
                }
            }
        }
    ],
        "next_cursor": None,
        "object": "list",
        "has_more": False
    }
}


class TestDatabaseParser(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestDatabaseParser.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    @responses.activate
    def test_database(self):
        body = RESPONSE_BODIES['get_database']
        uid = body['id']
        endpoint = f'{URL}/{uid}'

        responses.add(responses.GET, endpoint, json=body, status=200)
        req = requests.get(endpoint)
        obj = parse_database(req)
        debug_json(self.logger, 'DatabaseModel', json.loads(obj.json()))
        self.assertIsInstance(obj, DatabaseModel)

    @responses.activate
    def test_list(self):
        endpoint = URL
        body = RESPONSE_BODIES['get_all_databases']
        responses.add(responses.GET, endpoint, json=body, status=200)

        req = requests.get(endpoint)
        obj = parse_database_list(req)
        debug_json(self.logger, 'DatabaseModel List', json.loads(obj.json()))
        self.assertIsInstance(obj, ResponseListModel)


if __name__ == "__main__":
    main()
