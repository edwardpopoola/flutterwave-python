from utils import Utils

class Disburse(Utils):
    """Flutterwave Disburse module

        Provides methods for running transactions between accounts
    """

    def __init__(self, util):
        self.util = util

    
    def send(self, requestData):
        """Request a disburse to a destination account.
        
        amount        -> Amount to credit recipient (1000.00)
        ref           -> a transaction reference you will provide for tracking
        narration     -> Description to include in the transaction
        creditAccount -> Account to credit
        recipientName -> Transaction recipient name
        bankCode      -> Recipients Bankcode
        senderName    -> Transaction sender name
        country       -> Country code (NGN)
        currency      -> Transaction Currency
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "transferamount": self.util.encryptData(requestData['amount']),
            "uniquereference": self.util.encryptData(requestData['ref']),
            "destbankcode": self.util.encryptData(requestData['bankCode']),
            "narration": self.util.encryptData(requestData['narration']),
            "recipientaccount": self.util.encryptData(requestData['creditAccount']),
            "recipientname": self.util.encryptData(requestData['recipientName']),
            "sendername": self.util.encryptData(requestData['senderName']),
            "country": self.util.encryptData(requestData['country']),
            "currency": self.util.encryptData(requestData['currency'])
        }
        return self.util.sendRequest(self.util.disburseSendRoute, payload);

    
    

