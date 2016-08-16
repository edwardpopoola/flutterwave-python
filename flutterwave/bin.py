from utils import Utils

class Bin(Utils):
    """Flutterwave BIN class
    """

    def __init__(self, apiKey, merchantKey):
        self.apiKey = apiKey
        self.merchantKey = merchantKey


    def check(self, cardBin):
        """Request card details using Bin
        
        cardBin -> First 6-digits of card BIN
        '"""
        payload = {
            'card6': cardBin
        }
        return super(Bin, self).sendRequest(Utils.binCheckRoute, payload)
