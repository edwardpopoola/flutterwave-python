from utils import Utils

class Ip(object):
    """Flutterwave IP class
    """

    def __init__(self, util):
        self.util = util


    def check(self, ipAddress, country):
        """Request location and information on a specified IP
        
        ipAddress -> IP address to search
        country -> Country code (NGN)
        '"""
        payload = {
            'ip': ipAddress,
            'country': country
        }
        return self.util.sendRequest(self.util.ipCheckRoute, payload)
