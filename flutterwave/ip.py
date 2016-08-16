from utils import Utils

class Ip(Utils):
    """Flutterwave IP class
    """

    def __init__(self, apiKey, merchantKey):
        self.apiKey = apiKey
        self.merchantKey = merchantKey


    def check(self, ipAddress):
        """Request location and information on a specified IP
        
        ipAddress -> IP address to search
        '"""
        payload = {
            'ip': ipAddress
        }
        return super(Ip, self).sendRequest(Utils.ipCheckRoute, payload)
