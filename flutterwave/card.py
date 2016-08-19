from utils import Utils

class Card(Utils):
    """Flutterwave Card module

        Provides methods for charging a credit / debit card
    """

    def __init__(self, util):
        self.util = util


    def tokenize(self, requestData):
        """Request a card token
        Card tokens can be used to charge cards without card details.
        
        validateOption  -> verification method to use - Voice, SMS
        authModel       -> authentication Model - BVN, PIN, NOAUTH
        cardNumber      -> Card Number
        cvv             -> Card CVV
        expiryMonth     -> Card expiry month
        expiryYear      -> Card expiry year
        bvn             -> (Optional) User BVN, required only for authModel=BVN
        country         -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "validateoption": self.util.encryptData(requestData['validateOption']),
            "authmodel": self.util.encryptData(requestData['authModel']),
            "cardno": self.util.encryptData(requestData['cardNumber']),
            "cvv": self.util.encryptData(requestData['cvv']),
            "expirymonth": self.util.encryptData(requestData['expiryMonth']),
            "expiryyear": self.util.encryptData(requestData['expiryYear']),
            "bvn": self.util.encryptData(requestData['bvn']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.cardTokenizeRoute, payload);


    def charge(self, requestData):
        """Request to charge a card 
        
        amount          -> Amount to debit from card
        authModel       -> authentication Model - BVN, PIN, NOAUTH, VBVSECURECODE
        cardNumber      -> Card Number
        cvv             -> Card CVV
        expiryMonth     -> Card expiry month
        expiryYear      -> Card expiry year
        currency        -> Transaction currency
        customerID      -> Customer ID for tracking charge transaction
        narration       -> Transaction description
        responseUrl     -> Callback Url
        cardtype        -> (Optional) Card type - Diamound
        bvn             -> (Optional) User BVN, required only for authModel=BVN
        country         -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "amount": self.util.encryptData(requestData['amount']),
            "authmodel": self.util.encryptData(requestData['authModel']),
            "cardno": self.util.encryptData(requestData['cardNumber']),
            "currency": self.util.encryptData(requestData['currency']),
            "custid":  self.util.encryptData(requestData['customerID']),
            "cvv": self.util.encryptData(requestData['cvv']),
            "expirymonth": self.util.encryptData(requestData['expiryMonth']),
            "expiryyear": self.util.encryptData(requestData['expiryYear']),
            "narration": self.util.encryptData(requestData['narration']),
            "responseurl": self.util.encryptData(requestData['responseUrl']),
            "country": self.util.encryptData(requestData['country'])
        }

        if('bvn' in requestData):
            payload["bvn"] = self.util.encryptData(requestData['bvn'])

        if('cardtype' in requestData):
            payload["cardtype"] = self.util.encryptData(requestData['cardtype']),

        return self.util.sendRequest(self.util.cardChargeRoute, payload);


    def chargeWithToken(self, requestData):
        """Request to charge a card using a card token
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        customerID      -> Customer ID for tracking charge transaction
        narration       -> Transaction description
        cardtype        -> (Optional) Card type - Diamound
        country         -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "amount": self.util.encryptData(requestData['amount']),
            "currency": self.util.encryptData(requestData['currency']),
            "custid": self.util.encryptData(requestData['customerID']),
            "narration": self.util.encryptData(requestData['narration']),
            "chargetoken": self.util.encryptData(requestData['cardToken']),
            "country": self.util.encryptData(requestData['country'])
        }

        if('cardtype' in requestData):
            payload["cardtype"] = self.util.encryptData(requestData['cardtype']),

        return self.util.sendRequest(self.util.cardChargeRoute, payload);


    def validate(self, requestData):
        """Request to validate a card charge transaction
        
        otp                      -> otp
        otpTransactionIdentifier -> Transaction reference from card charge / tokenize request
        cardtype                 -> (Optional) Card type - Diamound
        country                  -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "otp": self.util.encryptData(requestData['otp']),
            "otptransactionidentifier": self.util.encryptData(requestData['otpTransactionIdentifier']),
            "country": self.util.encryptData(requestData['country'])
        }

        if('cardtype' in requestData):
            payload["cardtype"] = self.util.encryptData(requestData['cardtype']),

        return self.util.sendRequest(self.util.cardValidateRoute, payload);


    def preauth(self, requestData):
        """Request a PreAuthorization / Hold on a card for a specified amount
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        country         -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "amount": self.util.encryptData(requestData['amount']),
            "currency": self.util.encryptData(requestData['currency']),
            "chargetoken": self.util.encryptData(requestData['cardToken']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.cardPreauthRoute, payload);


    def capture(self, requestData):
        """Request a Capture / Accept on a preauthorized amount on a card
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        transactionRef  -> Transaction reference from a preauthorize request
        authorizeID     -> Authorize ID from a preauthorize request
        country         -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "amount": self.util.encryptData(requestData['amount']),
            "currency": self.util.encryptData(requestData['currency']),
            "trxreference": self.util.encryptData(requestData['transactionRef']),
            "trxauthorizeid": self.util.encryptData(requestData['authorizeID']),
            "country": self.util.encryptData(requestData['country'])
        }

        return self.util.sendRequest(self.util.cardCaptureRoute, payload);


    def refund(self, requestData):
        """Request a Refund on a charged card
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        transactionRef  -> Transaction reference from a preauthorize request
        authorizeID     -> Authorize ID from a preauthorize request
        country         -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "amount": self.util.encryptData(requestData['amount']),
            "currency": self.util.encryptData(requestData['currency']),
            "trxreference": self.util.encryptData(requestData['transactionRef']),
            "trxauthorizeid": self.util.encryptData(requestData['authorizeID']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.cardRefundRoute, payload);


    def void(self, requestData):
        """Request a Refund on a charged card
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        transactionRef  -> Transaction reference from a preauthorize request
        authorizeID     -> Authorize ID from a preauthorize request
        country         -> Country code (NGN)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "amount": self.util.encryptData(requestData['amount']),
            "currency": self.util.encryptData(requestData['currency']),
            "trxreference": self.util.encryptData(requestData['transactionRef']),
            "trxauthorizeid": self.util.encryptData(requestData['authorizeID']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.cardVoidRoute, payload);


