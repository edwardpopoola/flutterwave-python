from utils import Utils
from ip import Ip
from bvn import Bvn
from account import Account
from bin import Bin
from disburse import Disburse
from card import Card
from bank import Bank

class Flutterwave():
    """The Flutterwave Class

        Attributes:
        apiKey: Api key required for authenciated requests to the Flutterwave service
        merchantKey: Merchant Key required for identifying the merchant on the Flutterwave service
        options: (Optional) An array of optional initialization parameters
            baseUrl: Set a baseurl for requests
            debug: Turn on request debugging
    """

    def __init__(self, apiKey, merchantKey, options={}):

        self.util = Utils(apiKey, merchantKey)

        if("baseUrl" in options):
            self.util.setBaseUrl(options["baseUrl"])

        if("debug" in options):
            self.util.enableDebug(options["debug"])


        self.ip = Ip(self.util)
        self.bvn = Bvn(self.util)
        self.account = Account(self.util)
        self.bin = Bin(self.util)
        self.disburse = Disburse(self.util)
        self.card = Card(self.util)
        self.bank = Bank(self.util)

