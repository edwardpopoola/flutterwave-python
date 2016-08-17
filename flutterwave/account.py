
class Account(object):
    """Flutterwave Accounts module

        Provides methods for running transactions between accounts
    """

    def __init__(self, util):
        self.util = util

    
    def tokenize(self, accountNumber):
        """Request to tokenize an account
        
        requestData.accountNumber  -> Account number to tokenize
        '"""
        payload = {
            "accountNumber": self.util.encryptData(accountNumber),
            "merchantid": self.util.merchantKey
        }
        return self.util.sendRequest(self.util.accountTokenizeRoute, payload);


    def validate(self, requestData):
        """Request to validate account tokenization
        
        requestData.accountNumber -> Account number to 
        requestData.amount        -> Amount to debit from account (1000.00)
        requestData.ref           -> Transaction reference from the tokenize request
        requestData.otp           -> OTP to verify tokenize request
        requestData.narration     -> Transaction description
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "accountNumber": self.util.encryptData(requestData['accountNumber']),
            "otp": self.util.encryptData(requestData['otp']),
            "reference": self.util.encryptData(requestData['ref']),
            "billingamount": self.util.encryptData(requestData['amount']),
            "narration": self.util.encryptData(requestData['narration']),
        }
        return self.util.sendRequest(self.util.accountValidateRoute, payload);


    def charge(self, requestData):
        """Request to charge an account using an account token
        
        requestData.token     -> Token from previously tokenized account
        requestData.amount    -> Amount to debit from account
        requestData.narration -> Transaction description
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "accountToken": self.util.encryptData(requestData['token']),
            "billingamount": self.util.encryptData(requestData['amount']),
            "debitnarration": self.util.encryptData(requestData['narration'])
        }
        return self.util.sendRequest(self.util.accountChargeRoute, payload);

    
    

