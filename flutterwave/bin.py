from utils import Utils

class Bin(Utils):
    """Flutterwave BIN class
    """

    def __init__(self, util):
        self.util = util


    def check(self, cardBin, country):
        """Request card details using Bin
        
        cardBin -> First 6-digits of card BIN
        country -> Country code (NGN)
        '"""
        payload = {
            "card6": cardBin,
            "country": country
        }
        return self.util.sendRequest(self.util.binCheckRoute, payload)
