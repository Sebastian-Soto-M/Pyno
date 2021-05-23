from pyno.models.requests import NotionApi
import logging
import sys
from unittest import TestCase, skip, main

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


class TestUser(TestCase):

    @skip("Skipped Test Case")
    @classmethod
    def setUpClass(cls):
        logger.info('-------Started: Logging Api User--------')

    @classmethod
    def tearDownClass(cls):
        logger.info('-------Finished: Logging Api User-------')

    def test_get_user(self):
        logger.info('TEST: test_get_users')
        uid = "848e2e82-bc8c-498b-8e84-396d73a11229"
        usr = NotionApi.get_user(uid)
        logger.debug(usr)
        self.assertEqual(usr.name, 'Sebastian Soto')

    def test_get_all_users_page_size(self):
        logger.info('TEST: test_get_all_users_page_size')
        usr_lst_resp = NotionApi.get_all_users(page_size=1)
        self.assertTrue(usr_lst_resp.has_more)

    def test_get_all_users_start_cursor(self):
        logger.info('TEST: test_get_all_users_start_cursor')
        usr_lst_resp = NotionApi.get_all_users(start_cursor="")
        logger.debug(usr_lst_resp)

    def test_get_all_users_no_params(self):
        logger.info('TEST: test_get_all_users_no_params')
        usr_lst_resp = NotionApi.get_all_users()
        logger.debug(usr_lst_resp)
        self.assertEqual(len(usr_lst_resp.results), 2)


class TestApiDatabase(TestCase):
    DATABASE_ID = "5f7f1bcdfff04414ac5cd7099b871726"

    @skip("Skipped Test Case")
    @classmethod
    def setUpClass(cls):
        logger.info('-------Started: Logging Api Database--------')

    @classmethod
    def tearDownClass(cls):
        logger.info('-------Finished: Logging Api Database-------')

    def test_query_database(self):
        logger.info('TEST: test_query_database')

    def test_retrieve_database(self):
        logger.info('TEST: test_retrieve_database')
        db = NotionApi.get_database(self.DATABASE_ID)
        logger.debug(db)
        self.assertEqual(db.id.replace('-', ''), self.DATABASE_ID)

    def test_list_databases(self):
        pass


class TestPage(TestCase):

    @skip("Skipped Test Case")
    def setUp(self):
        pass

    def test_retrieve_page(self):
        pass

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
