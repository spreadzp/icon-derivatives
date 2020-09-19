from iconservice import *
import json
import base64

TAG = "TradeBoard"


class PriceInterface(InterfaceScore):

    @interface
    def get_last_price_block(self) -> dict: pass
    def set_price(self, price: int) -> None: pass


class TradeBoard(IconScoreBase):
    rateDeposit = 0.002
    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        # self.score_oracle = ScoreWithPycharm(db)
        self.derivatives = VarDB("derivatives", db, value_type=str)
        self.last_price = VarDB("last_price", db, value_type=int)
        self.block_number = VarDB("block_number", db, value_type=int)
        self.bankOfDerivative = VarDB("bankOfDerivative", db, value_type=int)
        self.investor_address = VarDB(
            "investor_address", db, value_type=Address)

    @eventlog(indexed=2)
    def SetPrice(self, message: str, newPrice: int): pass

    @eventlog(indexed=1)
    def SetAddressValue(self, value: str): pass

    @eventlog(indexed=1)
    def TestInfo(self, value: str): pass

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def get_last_price_info(self) -> dict:
        Logger.debug(f"Price!")
        return {"price": self.last_price.get(), "blockNumber": self.block_number.get() }

    @external
    def set_last_price(self, _price: int, _block_number: int)-> None:
        # if self.owner and self.msg.sender:
        self.last_price.set(_price)
        self.block_number.set(_block_number)
        self.SetPrice("New price: ", self.last_price.get())
    # else:
    # revert(self.msg.sender)

    @external(readonly=True)
    def define_price_in_token(self, _сurrent_price: int, _price_expiration: int) -> int:
        # if self.owner and self.msg.sender:
        return round(( _price_expiration * 1000) / 10 / _сurrent_price)

    @external(readonly=True)
    def get_active_derivative(self) -> str:
        derivative = self.derivatives.get()
        self.TestInfo(derivative)
        return derivative

    @external(readonly=True)
    def get_investor_address(self) -> Address:
        inv = self.investor_address.get()
        self.TestInfo(inv)
        return inv

    @external
    def create_derivative(self, expirationPrice: int, expirationBlock: int, infoDerivative: str):
        newDerivative = {"nameDerivative": infoDerivative, "expirationPrice": expirationPrice, "currentPrice": 45, "blockExpiration": expirationBlock, "timeExpiration": 12345678989, "deposit": 50}
        Logger.debug(f"Data from :", "newDerivative")
        self.derivatives.set(f"{newDerivative}")

    @external
    def define_profit_investors(self):
        Logger.debug(f"Data from :", TAG)


    @external
    def make_order(self, direction: str, nameOfDerivative: str )-> None:
        Logger.debug(f"Data from :", TAG)

    @external
    def expire_derivative(self, expirePrice: int, currentBlock: int, nameOfDerivative: str) -> int:
        current_derivative: str =  self.derivatives.get()
        Logger.debug(f"Data from!!!!!!!!!! :", current_derivative)
        data_deserealized = eval(json.loads(json.dumps(current_derivative)))
        if 1 <= currentBlock:
          return self.block # data_deserealized['nameDerivative']
        else :
          return current_derivative

    @external
    def buy_goal_price(self, buyer_address: Address, expirationPrice: int, amount: int, expirationBlock: int) -> int:
        ticket = {"investorAddress": buyer_address, "expirationPrice": expirationPrice, "currentPrice": 45, "blockExpiration": expirationBlock, "timeExpiration": 12345678989, "deposit": amount}
        self.investor_address.set(buyer_address)
        Logger.debug(f"Data from :", "ticket")
        self.derivatives.set(f"{ticket}")

    @external
    def makeDeposit(self, buyer_address: Address, depositeTime: int, amount: int) -> int:
        deposit = amount 
        self.derivatives.set(f"{deposit}")

    @external
    def withdrawDeposit(self, buyer_address: Address) -> int:

        self.derivatives.set(f"{ticket}")
