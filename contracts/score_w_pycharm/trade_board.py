from .price_oracle import PriceOracle
from iconservice import *

TAG = 'TradeBoard'


class TradeBoard(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        # self.score_oracle = PriceOracle(db)
        self.score_oracle = self.create_interface_score(
            PriceOracle, PriceInterface)

        # "cxe3a8300fe3f3abeb38e0d83a857f4de48e94be0f", PriceInterface)
        self.lastPrice = VarDB("lastPrice", db, value_type=int)
        self.bankOfDerivative = VarDB("bankOfDerivative", db, value_type=int)
        self.investor_address = VarDB(
            "investor_address", db, value_type=Address)

    @eventlog(indexed=0)
    def SetPrice(self, message: str, newPrice: int): pass

    @eventlog(indexed=1)
    def SetAddressValue(self, value: str): pass

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def get_last_price_info(self) -> dict:
        Logger.debug(f'Price!')
        return self.score_oracle.get_last_price_and_block()

    @external
    def set_last_price(self, price: int):
        # if self.owner and self.msg.sender:
        self.score_oracle.set_price(price)
        self.SetPrice("New price: ", self.lastPrice)
    # else:
    # revert(self.msg.sender)

    @external(readonly=True)
    def getActiveDerivative(self) -> dict:
        Logger.debug(f'Data from :', TAG)
        derivatives = [{'nameDerivative': 'opion 55', 'expirationPrice': 55, 'currentPrice': 45, 'blockExpiration': 123456, 'timeExpiration': 12345678989, 'deposit': 50},
                       {'nameDerivative': 'opion 65', 'expirationPrice': 65, 'currentPrice': 45,
                           'blockExpiration': 123456, 'timeExpiration': 12345678989, 'deposit': 60}
                       ]
        return derivatives

    @external
    def createDerivative(self, expirationPrice: int, expirationBlock: int, infoDerivative: str) -> dict:
        Logger.debug(f'Data from :', TAG)
        derivatives = [{'nameDerivative': 'opion 55', 'expirationPrice': 55, 'currentPrice': 45, 'blockExpiration': 123456, 'timeExpiration': 12345678989, 'deposit': 50},
                       {'nameDerivative': 'opion 65', 'expirationPrice': 65, 'currentPrice': 45,
                           'blockExpiration': 123456, 'timeExpiration': 12345678989, 'deposit': 60}
                       ]
        return derivatives

    @external
    def define_profit_investors(self) -> dict:
        Logger.debug(f'Data from :', TAG)
        derivatives = [{'nameDerivative': 'opion 55', 'expirationPrice': 55, 'currentPrice': 45, 'blockExpiration': 123456, 'timeExpiration': 12345678989, 'deposit': 50},
                       {'nameDerivative': 'opion 65', 'expirationPrice': 65, 'currentPrice': 45,
                           'blockExpiration': 123456, 'timeExpiration': 12345678989, 'deposit': 60}
                       ]
        return derivatives


class PriceInterface(InterfaceScore):

    @interface
    def get_last_price_and_block(self) -> dict: pass
    def set_price(self, price: int) -> None: pass
