from .score_w_pycharm import ScoreWithPycharm
from iconservice import *

TAG = 'ScoreWithPycharm'


class FooInterface(InterfaceScore):

    @interface
    def get_price(self) -> int: pass
    def set_price(self, price: int) -> None: pass

class TradeBoard(IconScoreBase):


    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        # self.score_w = ScoreWithPycharm(db)
        self.score_w = self.create_interface_score(ScoreWithPycharm, FooInterface)
        self.lastPrice = VarDB("lastPrice", db, value_type=int)
        self.investor_address = VarDB("investor_address", db, value_type=Address)

    @eventlog(indexed=0)
    def SetPrice(self, message: str, newPrice: int): pass

    @eventlog(indexed=1)
    def SetAddressValue(self, value: str): pass

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return "Hello"

    @external(readonly=True)
    def get_last_price(self) -> int:
        Logger.debug(f'Price!')
        return self.score_w.get_price()

    @external
    def set_last_price(self, price: int):
    # if self.owner and self.msg.sender:
      self.score_w.set_price(price)
      self.SetPrice("New price: ", self.lastPrice)
    # else:
    # revert(self.msg.sender)
