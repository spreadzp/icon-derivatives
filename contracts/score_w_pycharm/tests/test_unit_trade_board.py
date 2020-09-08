from ..trade_board import TradeBoard
from ..price_oracle import PriceOracle
from tbears.libs.scoretest.score_test_case import ScoreTestCase
import json


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
        self.score.set_last_price(price, block)
        self.assertEqual(self.score.get_last_price_info(), {"price": price, "blockNumber": block})

    def test_define_price_in_token(self):
        current_price = 0.45
        expiration_price = 0.55
        expect_amount = 122
        print("define_price_in_token")
        print(self.test_account1)
        print(self.score.owner)
        print(self.score.msg.sender)
        self.assertEqual(self.score.define_price_in_token(current_price, expiration_price), expect_amount)

    def test_get_active_derivative(self):
        expirationPrice = 12
        expirationBlock = 35687
        infoDerivative = "ABC"
        print("test_get_active_derivative")
        print(self.test_account1)
        print(self.score.owner)
        print(self.score.msg.sender)

        # resJson = json.load(str(resStr)
        self.score.create_derivative(expirationPrice, expirationBlock, infoDerivative)
        resStr = self.score.get_active_derivative()

        print(resStr)
        print("@@@@@@@@@@")
        test_info = {"nameDerivative": infoDerivative, "expirationPrice": expirationPrice, "currentPrice": 45, "blockExpiration": expirationBlock, "timeExpiration": 12345678989, "deposit": 50}
        self.assertEqual(resStr, f"{test_info}")

    def test_expire_derivative(self):
        expirationPrice = 12
        expirationBlock = 35688
        infoDerivative = "ABC"
        print("test_expire_derivative")


        # resJson = json.load(str(resStr)
        self.score.create_derivative(expirationPrice, expirationBlock, infoDerivative)
        resStr = self.score.expire_derivative(expirationPrice, expirationBlock, infoDerivative)

        print(resStr)
        print("!!!!!")
        self.assertEqual(resStr, 35687)
