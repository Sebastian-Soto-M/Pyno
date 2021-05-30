import logging
import sys
import time
from unittest import TestCase, main, skip

from pyno.api import NotionApi
from pyno.api.request import CreatePageRequestModel

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(module)s|%(name)s:\t%(message)s')


class TestUser(TestCase):

    # @skip("Skipped Test Case")
    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)
        cls.logger.info('-------Started: Logging Api User--------')

    @classmethod
    def tearDownClass(cls):
        cls.logger.info('-------Finished: Logging Api User-------')

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        self.logger.info('%s: %.3f' % (self.id(), t))

    def test_get_user(self):
        uid = "848e2e82-bc8c-498b-8e84-396d73a11229"
        usr = NotionApi.get_user(uid)
        self.assertEqual(usr.name, 'Sebastian Soto')

    @skip("Skipped Test Case")
    def test_get_all_users_page_size(self):
        usr_lst_resp = NotionApi.get_all_users(page_size=1)
        self.assertTrue(usr_lst_resp.has_more)

    @skip("Skipped Test Case")
    def test_get_all_users_start_cursor(self):
        usr_lst_resp = NotionApi.get_all_users(start_cursor="")
        self.logger.debug(usr_lst_resp)

    @skip("Skipped Test Case")
    def test_get_all_users_no_params(self):
        usr_lst_resp = NotionApi.get_all_users()
        self.logger.debug(usr_lst_resp)
        self.assertEqual(len(usr_lst_resp.results), 2)



if __name__ == "__main__":
    main()
