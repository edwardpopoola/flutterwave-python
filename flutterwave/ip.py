from utils import Utils

class Ip(object):
    """Flutterwave IP class
    """

    def __init__(self, util):
        self.util = util


    def check(self, ipAddress):
        """Request location and information on a specified IP
        
        ipAddress -> IP address to search
        '"""
        payload = {
            'ip': ipAddress
        }
        return self.util.sendRequest(self.util.ipCheckRoute, payload)
