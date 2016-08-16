from utils import Utils

class Account(Utils):
    """Flutterwave Accounts module

        Provides methods for running transactions between accounts
    """

    def __init__(self, apiKey, merchantKey):
        self.apiKey = apiKey
        self.merchantKey = merchantKey

    
    def tokenize(self, accountNumber):
        """Request to tokenize an account
        
        requestData.accountNumber  -> Account number to tokenize
        '"""
        payload = {
            "accountNumber": super(Account, self).encrypData(self.apiKey, accountNumber),
            "merchantid": self.merchantKey
        }
        return super(Account, self).sendRequest(Utils.accountTokenizeRoute, payload);


    def validate(self, requestData):
        """Request to validate account tokenization
        
        requestData.accountNumber -> Account number to 
        requestData.amount        -> Amount to debit from account (1000.00)
        requestData.ref           -> Transaction reference you will provide for tracking
        requestData.otp           -> OTP to verify tokenize request
        requestData.narration     -> Transaction description
        '"""
        payload = {
            "merchantid": self.merchantKey,
            "accountNumber": super(Account, self).encrypData(self.apiKey, requestData['accountNumber']),
            "otp": super(Account, self).encrypData(self.apiKey, requestData['otp']),
            "reference": super(Account, self).encrypData(self.apiKey, requestData['ref']),
            "billingamount": super(Account, self).encrypData(self.apiKey, requestData['amount']),
            "narration": super(Account, self).encrypData(self.apiKey, requestData['narration']),
        }
        return super(Account, self).sendRequest(Utils.accountValidateRoute, payload);


    def charge(self, requestData):
        """Request to charge an account using an account token
        
        requestData.token     -> Token from previously tokenized account
        requestData.amount    -> Amount to debit from account
        requestData.narration -> Transaction description
        '"""
        payload = {
            "merchantid": self.merchantKey,
            "accountToken": super(Account, self).encrypData(self.apiKey, requestData['token']),
            "billingamount": super(Account, self).encrypData(self.apiKey, requestData['amount']),
            "debitnarration": super(Account, self).encrypData(self.apiKey, requestData['narration'])
        }
        return super(Account, self).sendRequest(Utils.accountChargeRoute, payload);

    
    

