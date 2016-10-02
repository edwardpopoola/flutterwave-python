
class Account(object):
    """Flutterwave Accounts module

        Provides methods for running transactions between accounts
    """

    def __init__(self, util):
        self.util = util

    
    def tokenize(self, accountNumber, country):
        """Request to tokenize an account
        
        requestData.accountNumber  -> Account number to tokenize
        country                    -> Country code (NGN)
        '"""
        payload = {
            "accountNumber": self.util.encryptData(accountNumber),
            "merchantid": self.util.merchantKey,
            "country": self.util.encryptData(country)
        }
        return self.util.sendRequest(self.util.accountTokenizeRoute, payload);


    def validate(self, requestData):
        """Request to validate account tokenization
        
        requestData.accountNumber -> Account number requesting token
        requestData.amount        -> Amount to debit from account (1000.00)
        requestData.ref           -> Transaction reference from the tokenize request
        requestData.otp           -> OTP to verify tokenize request
        requestData.narration     -> Transaction description
        requestData.country       -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "accountNumber": self.util.encryptData(requestData['accountNumber']),
            "otp": self.util.encryptData(requestData['otp']),
            "reference": self.util.encryptData(requestData['ref']),
            "billingamount": self.util.encryptData(requestData['amount']),
            "narration": self.util.encryptData(requestData['narration']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.accountValidateRoute, payload);


    def charge(self, requestData):
        """Request to charge an account using an account token
        
        requestData.token     -> Token from previously tokenized account
        requestData.amount    -> Amount to debit from account
        requestData.narration -> Transaction description
        requestData.country   -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "accountToken": self.util.encryptData(requestData['token']),
            "billingamount": self.util.encryptData(requestData['amount']),
            "debitnarration": self.util.encryptData(requestData['narration']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.accountChargeRoute, payload);


    def lookup(self, requestData):
        """Request to lookup an account number, returns account details.
        
        requestData.destBankCode        -> Destination Bank code for the account number
        requestData.recipientAccount    -> Account number
        requestData.country             -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "destbankcode": self.util.encryptData(requestData['destBankCode']),
            "recipientaccount": self.util.encryptData(requestData['recipientAccount']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.accountLookupRoute, payload);


    def chargeAny(self, requestData):
        """Request to charge any Nigerian bank account
        
        requestData.narration      -> Transaction description
        requestData.accountNumber  -> Customer's account number
        requestData.bankCode       -> Customer's bank code
        requestData.passcode       -> 12 digit string as passcode
        requestData.amount         -> Amount to debit from account
        requestData.currency       -> Transaction currency
        requestData.firstName      -> Customer first name
        requestData.lastName       -> Customer last name
        requestData.email          -> Customer email
        requestData.transactionRef -> Your tracking reference
        requestData.country        -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "narration": self.util.encryptData(requestData['narration']),
            "accountnumber": self.util.encryptData(requestData['accountNumber']),
            "bankcode": self.util.encryptData(requestData['bankCode']),
            "passcode": self.util.encryptData(requestData['passcode']),
            "amount": self.util.encryptData(requestData['amount']),        
            "currency": self.util.encryptData(requestData['currency']),      
            "firstname": self.util.encryptData(requestData['firstName']),
            "lastname": self.util.encryptData(requestData['lastName']),
            "email": self.util.encryptData(requestData['email']),
            "transactionreference": self.util.encryptData(requestData['transactionRef']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.accountChargeAnyRoute, payload);


    def validateChargeAnyRef(self, requestData):
        """Request to a chargeAny transaction using transaction reference
        
        requestData.transactionRef -> Transaction Ref from chargeAny request
        requestData.otp            -> otp to verify chargeAny request
        requestData.country        -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "otp": self.util.encryptData(requestData['otp']),
            "transactionreference": self.util.encryptData(requestData['transactionRef']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.accountValidateChargeAnyRefRoute, payload);


    def validateChargeAnyPhone(self, requestData):
        """Request to a chargeAny transaction using phonenumber
        
        requestData.phoneNumber -> Customer phone used in chargeAny request
        requestData.otp         -> otp to verify chargeAny request
        requestData.country     -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "otp": self.util.encryptData(requestData['otp']),
            "phonenumber": self.util.encryptData(requestData['phoneNumber']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.accountValidateChargeAnyPhoneRoute, payload);
