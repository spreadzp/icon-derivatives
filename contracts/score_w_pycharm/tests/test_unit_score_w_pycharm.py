from ..score_w_pycharm import ScoreWithPycharm
from tbears.libs.scoretest.score_test_case import ScoreTestCase


class TestScoreWithPycharm(ScoreTestCase):

    def setUp(self):
        super().setUp()
        self.score = self.get_score_instance(ScoreWithPycharm, self.test_account1)

    def test_hello(self):
        self.assertEqual(self.score.hello(), "Hello")

    def test_get_price(self):
        price = 12548
        print("+++++++++++++")
        print(self.test_account1)
        print(self.score.owner)
        print(self.score.msg.sender)
        self.score.set_price(price)
        self.assertEqual(self.score.get_price(), price)
