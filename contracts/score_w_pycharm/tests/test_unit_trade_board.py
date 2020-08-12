from ..trade_board import TradeBoard
from ..price_oracle import PriceOracle
from tbears.libs.scoretest.score_test_case import ScoreTestCase


class TestTradeBoard(ScoreTestCase):

    def setUp(self):
        super().setUp()
        self.scorePrice = self.get_score_instance(
            PriceOracle, self.test_account1)
        self.score = self.get_score_instance(TradeBoard, self.test_account1)

    def test_get_last_price(self):
        price = 12548
        block = 35687
        print("TradeBoard test_get_last_price")
        print(self.test_account1)
        print(self.score.owner)
        print(self.score.msg.sender)
        self.scorePrice.set_price(price, block)
        self.assertEqual(self.score.get_last_price_info(), {'price': price, 'blockNumber': block})