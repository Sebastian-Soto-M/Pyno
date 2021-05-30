class TestApiDatabase(TestCase):
    DATABASE_ID = "5f7f1bcdfff04414ac5cd7099b871726"

    @skip("Skipped Test Case")
    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)
        cls.logger.info('-------Started: Logging Api Database--------')

    @classmethod
    def tearDownClass(cls):
        cls.logger.info('-------Finished: Logging Api Database-------')

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        self.logger.info('%s: %.3f' % (self.id(), t))

    def test_query_database(self):
        self.logger.info('TEST: test_query_database')

    def test_retrieve_database(self):
        self.logger.info('TEST: test_retrieve_database')
        db = NotionApi.get_database(self.DATABASE_ID)
        self.logger.debug(db)
        self.assertEqual(db.id.replace('-', ''), self.DATABASE_ID)

    def test_list_databases(self):
        self.logger.info('TEST: test_list_database')
        db_list = NotionApi.get_all_databases()
        self.logger.debug(db_list)


class TestPage(TestCase):
    DATABASE_ID = "ed0cac1b641f4a3c9ca3e0bf6145d216"
    DATA = {
        "parent": {"database_id": "48f8fee9cd794180bc2fec0398253067"},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "Tuscan Kale"
                        }
                    }
                ]
            },
            "Description": {
                "rich_text": [
                    {
                        "text": {
                            "content": "A dark green leafy vegetable"
                        }
                    }
                ]
            },
            "Food group": {
                "select": {
                    "name": "Vegetable"
                }
            },
            "Price": {"number": 2.5}
        },
        "children": [
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                        "text": [{"type": "text", "text": {"content": "Lacinato kale"}}]
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                        "text": [
                            {
                                "type": "text",
                                "text": {
                                        "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                                        "link": {"url": "https://en.wikipedia.org/wiki/Lacinato_kale"}
                                }
                            }
                        ]
                }
            }
        ]
    }

    @skip("Skipped Test Case")
    def setUp(self):
        pass

    def test_retrieve_page(self):
        # cpr = CreatePageRequestModel.parse_obj(self.data)
        # logger.info(cpr.properties.keys())
        res = NotionApi.add_page_to_db(
            self.DATABASE_ID, self.DATA['properties'])
        print(res)

    def test_create_page(self):
        pass

    def test_update_page(self):
        pass


class TestBlock(TestCase):
    @skip("Skipped Test Case")
    def setUp(self):
        pass

    def test_retrieve_block_children(self):
        pass

    def test_append_block_children(self):
        pass


class TestSearch(TestCase):
    @skip("Skipped Test Case")
    def setUp(self):
        pass

    def test_query(self):
        pass

    def test_sort(self):
        pass

    def test_filter(self):
        pass


if __name__ == "__main__":
    main()
