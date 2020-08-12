from ..price_oracle import PriceOracle
from tbears.libs.scoretest.score_test_case import ScoreTestCase


class TestPriceOracle(ScoreTestCase):

    def setUp(self):
        super().setUp()
        self.scorePrice = self.get_score_instance(
            PriceOracle, self.test_account1)
    def test_get_last_price(self):
        price = 12548
        block = 35687
        print("TestPriceOracle")
        print(self.test_account1)
        self.scorePrice.set_price(price, block)
        self.assertEqual(self.scorePrice.get_last_price_and_block(), {'price': price, 'blockNumber': block})
        print("TestPriceOracle fine")
