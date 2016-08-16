from utils import Utils

class Disburse(Utils):
    """Flutterwave Disburse module

        Provides methods for running transactions between accounts
    """

    def __init__(self, apiKey, merchantKey):
        self.apiKey = apiKey
        self.merchantKey = merchantKey

    
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
            "merchantid": self.merchantKey,
            "transferamount": super(Disburse, self).encrypData(self.apiKey, requestData['amount']),
            "uniquereference": super(Disburse, self).encrypData(self.apiKey, requestData['ref']),
            "destbankcode": super(Disburse, self).encrypData(self.apiKey, requestData['bankCode']),
            "narration": super(Disburse, self).encrypData(self.apiKey, requestData['narration']),
            "recipientaccount": super(Disburse, self).encrypData(self.apiKey, requestData['creditAccount']),
            "recipientname": super(Disburse, self).encrypData(self.apiKey, requestData['recipientName']),
            "sendername": super(Disburse, self).encrypData(self.apiKey, requestData['senderName']),
            "country": super(Disburse, self).encrypData(self.apiKey, requestData['country']),
            "currency": super(Disburse, self).encrypData(self.apiKey, requestData['currency'])
        }
        return super(Disburse, self).sendRequest(Utils.disburseSendRoute, payload);

    
    

