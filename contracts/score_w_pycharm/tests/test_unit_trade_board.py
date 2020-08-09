from ..trade_board import TradeBoard
from ..score_w_pycharm import ScoreWithPycharm
from tbears.libs.scoretest.score_test_case import ScoreTestCase


class TestTradeBoard(ScoreTestCase):

    def setUp(self):
        super().setUp()
        self.scorePrice = self.get_score_instance(ScoreWithPycharm, self.test_account1)
        self.score = self.get_score_instance(TradeBoard, self.test_account1)

    def test_hello(self):
        self.assertEqual(self.score.hello(), "Hello")

    def test_get_last_price(self):
        price = 12548
        print("TradeBoard")
        print(self.test_account1)
        print(self.score.owner)
        print(self.score.msg.sender)
        self.score.set_last_price(price)
        self.assertEqual(self.score.get_last_price(), price)
