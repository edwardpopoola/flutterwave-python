from ip import Ip
from bvn import Bvn
from account import Account
from bin import Bin
from disburse import Disburse
from card import Card

class Flutterwave():
    """The Flutterwave Class

        Attributes:
        apiKey: Api key required for authenciated requests to the Flutterwave service
        merchantKey: Merchant Key required for identifying the merchant on the Flutterwave service
    """

    def __init__(self, apiKey, merchantKey):
        self.ip = Ip(apiKey, merchantKey)
        self.bvn = Bvn(apiKey, merchantKey)
        self.account = Account(apiKey, merchantKey)
        self.bin = Bin(apiKey, merchantKey)
        self.disburse = Disburse(apiKey, merchantKey)
        self.card = Card(apiKey, merchantKey)

