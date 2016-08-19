from utils import Utils

class Bank(Utils):
    """Flutterwave BIN class
    """

    def __init__(self, util):
        self.util = util


    def list(self):
        """Request Bank list and codes
        
        '"""
        return self.util.sendRequest(self.util.bankListRoute, {})
