from iconservice import *

TAG = 'PriceOracle'


class PriceOracle(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self.price = VarDB("price", db, value_type=int)
        self.block_number = VarDB("block_number", db, value_type=int)
        self.investor_address = VarDB(
            "investor_address", db, value_type=Address)

    @eventlog(indexed=0)
    def SetNewData(self, message: str, newPrice: int, newBlock: int): pass

    @eventlog(indexed=1)
    def SetAddressValue(self, value: str): pass

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def get_last_price_and_block(self) -> dict:
        Logger.debug(f'Price! and block')
        return  {'price': self.price.get(), 'blockNumber': self.block_number.get()}

    @external
    def set_price(self, newPrice: int, newBlockNumber: int) -> None:
        self.block_number.set(newBlockNumber)
        self.price.set(newPrice)
        self.SetNewData("New data: ", newPrice, newBlockNumber)
