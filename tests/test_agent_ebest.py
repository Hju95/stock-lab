from distutils.log import error
import unittest
from stocklab.agent.ebest import EBest
import inspect
import time

class TestEBest(unittest.TestCase):
    def setUp(self):
        self.ebest = EBest("DEMO")
        self.ebest.login()

    def tearDown(self):
        self.ebest.logout()


    def test_get_account_info(self):
        result = self.ebest.get_account_info()
        assert result is not None
        print(result)
        
    # def test_get_code_list(self):
    #     print(inspect.stack()[0][3])
    #     all_result = self.ebest.get_code_list("ALL")
    #     assert all_result is not None
    #     kosdaq_result = self.ebest.get_code_list("KOSDAQ")
    #     assert kosdaq_result is not None
    #     kospi_result = self.ebest.get_code_list("KOSPI")
    #     assert kospi_result is not None
    #     try:
    #         error_result = self.ebest.get_code_list("KOS")
    #     except:
    #         error_result = None
    #     assert error_result is None
    #     print("result:", len(all_result), len(kosdaq_result), len(kospi_result))


    # def test_get_code_list(self):
    #     print(inspect.stack()[0][3])
    #     result = self.ebest.get_code_list("ALL")
    #     assert result is not None
    #     print(len(result))

    # def test_get_stock_price_by_code(self):
    #     print(inspect.stack()[0][3])
    #     result = self.ebest.get_stock_price_by_code("005930", "2")
    #     assert result is not None
    #     print(result)

    # def test_get_credit_trend_by_code(self):
    #     print(inspect.stack()[0][3])
    #     result = self.ebest.get_credit_trend_by_code("005930", "20220304")
    #     assert result is not None
    #     print(result)

    # def test_get_short_trend_by_code(self):
    #     print(inspect.stack()[0][3])
    #     result = self.ebest.get_short_trend_by_code("005930", sdate="20220201", edate="20220228")
    #     assert result is not None
    #     print(result)

    # def test_get_agent_trend_by_code(self):
    #     print(inspect.stack()[0][3])
    #     result = self.ebest.get_agent_trend_by_code("005930", fromdt="20220201", todt="20220228")
    #     assert result is not None
    #     print(result)

    