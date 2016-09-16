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
        country         -> Country code (NG)
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
        authModel       -> authentication Model - BVN, PIN, NOAUTH, VBVSECURECODE (requires decryption)
        cardNumber      -> Card Number
        cvv             -> Card CVV
        expiryMonth     -> Card expiry month
        expiryYear      -> Card expiry year
        currency        -> Transaction currency
        customerID      -> Customer ID for tracking charge transaction
        narration       -> Transaction description
        bvn             -> (Optional) User BVN, required only for authModel=BVN
        pin             -> (Optional) User Card PIN, required only for authModel=PIN
        responseUrl     -> (Optional) Callback Url, required for authModel=VBVSECURECODE
        cardtype        -> (Optional) Card type - Diamound
        country         -> Country code (NG)
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
            "country": self.util.encryptData(requestData['country'])
        }

        if('pin' in requestData):
            payload["pin"] = self.util.encryptData(requestData['pin'])

        if('bvn' in requestData):
            payload["bvn"] = self.util.encryptData(requestData['bvn'])

        if('responseUrl' in requestData):
            payload["responseurl"] = self.util.encryptData(requestData['responseUrl'])

        if('cardtype' in requestData):
            payload["cardtype"] = self.util.encryptData(requestData['cardtype'])

        return self.util.sendRequest(self.util.cardChargeRoute, payload);


    def chargeWithToken(self, requestData):
        """Request to charge a card using a card token
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        customerID      -> Customer ID for tracking charge transaction
        narration       -> Transaction description
        cardtype        -> (Optional) Card type - Diamound
        country         -> Country code (NG)
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


    def verifyCharge(self, transactionRef, country):
        """Request to verify a charge transaction using the returned transaction reference
        
        transactionRef -> Transaction reference from a charge request
        country        -> Country code (NG)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "trxreference": self.util.encryptData(transactionRef),
            "country": self.util.encryptData(country)
        }

        return self.util.sendRequest(self.util.cardChargeVerifyRoute, payload);


    def validate(self, requestData):
        """Request to validate a card charge transaction
        
        otp                      -> otp
        otpTransactionIdentifier -> Transaction reference from card charge / tokenize request
        cardtype                 -> (Optional) Card type - Diamound
        country                  -> Country code (NG)
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
        country         -> Country code (NG)
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
        country         -> Country code (NG)
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
        country         -> Country code (NG)
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
        country         -> Country code (NG)
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


    def balanceEnquiry(self, requestData):
        """Request funds balance on a card
        
        cardNumber      -> Card Number
        cvv             -> Card CVV
        expiryMonth     -> Card expiry month
        expiryYear      -> Card expiry year
        pin             -> Card pin
        transactionRef  -> Your tracking reference
        country         -> Country code (NG)

        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "cardno": self.util.encryptData(requestData['cardNumber']),
            "cvv": self.util.encryptData(requestData['cvv']),
            "expirymonth": self.util.encryptData(requestData['expiryMonth']),
            "expiryyear": self.util.encryptData(requestData['expiryYear']),
            "pin": self.util.encryptData(requestData['pin']),
            "trxreference": self.util.encryptData(requestData['transactionRef']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.cardBalanceroute, payload);




    def validateBalanceEnquiry(self, requestData):
        """Validate a request for funds balance on a card
        
        otp                      -> Amount to debit from card
        otpTransactionIdentifier -> Transaction reference from card charge / tokenize request
        transactionRef           -> Transaction reference from a preauthorize request
        country                  -> Country code (NG)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "otp": self.util.encryptData(requestData['otp']),
            "otptransactionidentifier": self.util.encryptData(requestData['otpTransactionIdentifier']),
            "trxreference": self.util.encryptData(requestData['transactionRef']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.validateCardBalanceroute, payload);
