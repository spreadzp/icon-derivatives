from iconservice import *

TAG = 'ScoreWithPycharm'


class ScoreWithPycharm(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self.price = VarDB("price", db, value_type=int)
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
    def get_price(self) -> int:
        Logger.debug(f'Price!')
        return self.price.get()

    @external
    def set_price(self, price: int) -> None:
    # if self.owner and self.msg.sender:
      self.price.set(price)
      self.SetPrice("New price: ", price)
    # else:
    #   revert(self.msg.sender)
