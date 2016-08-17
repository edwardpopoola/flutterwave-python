from utils import Utils

class Disburse(Utils):
    """Flutterwave Disburse module

        Provides methods for running transactions between accounts
    """

    def __init__(self, util):
        self.util = util

    
    def send(self, requestData):
        """Request a disburse to a destination account.
        
        requestData.amount        -> Amount to credit recipient (1000.00)
        requestData.ref           -> a transaction reference you will provide for tracking
        requestData.narration     -> Description to include in the transaction
        requestData.creditAccount -> Account to credit
        requestData.recipientName -> Transaction recipient name
        requestData.bankCode      -> Recipients Bankcode
        requestData.senderName    -> Transaction sender name
        requestData.country       -> Country code
        requestData.currency      -> Transaction Currency
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

    
    

