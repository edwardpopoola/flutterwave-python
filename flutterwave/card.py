from utils import Utils

class Card(Utils):
    """Flutterwave Card module

        Provides methods for charging a credit / debit card
    """

    def __init__(self, apiKey, merchantKey):
        self.apiKey = apiKey
        self.merchantKey = merchantKey


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
        '"""
        payload = {
            "merchantid": self.merchantKey,
            "validateoption": super(Card, self).encrypData(self.apiKey, requestData['validateOption']),
            "authmodel": super(Card, self).encrypData(self.apiKey, requestData['authModel']),
            "cardno": super(Card, self).encrypData(self.apiKey, requestData['cardNumber']),
            "cvv": super(Card, self).encrypData(self.apiKey, requestData['cvv']),
            "expirymonth": super(Card, self).encrypData(self.apiKey, requestData['expiryMonth']),
            "expiryyear": super(Card, self).encrypData(self.apiKey, requestData['expiryYear']),
            "bvn": super(Card, self).encrypData(self.apiKey, requestData['bvn'])
        }
        return super(Card, self).sendRequest(Utils.cardTokenizeRoute, payload);


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
        '"""
        payload = {
            "merchantid": self.merchantKey,
            "amount": super(Card, self).encrypData(self.apiKey, requestData['amount']),
            "authmodel": super(Card, self).encrypData(self.apiKey, requestData['authModel']),
            "cardno": super(Card, self).encrypData(self.apiKey, requestData['cardNumber']),
            "currency": super(Card, self).encrypData(self.apiKey, requestData['currency']),
            "custid":  super(Card, self).encrypData(self.apiKey, requestData['customerID']),
            "cvv": super(Card, self).encrypData(self.apiKey, requestData['cvv']),
            "expirymonth": super(Card, self).encrypData(self.apiKey, requestData['expiryMonth']),
            "expiryyear": super(Card, self).encrypData(self.apiKey, requestData['expiryYear']),
            "narration": super(Card, self).encrypData(self.apiKey, requestData['narration']),
            "responseurl": super(Card, self).encrypData(self.apiKey, requestData['responseUrl']),
        }

        if('bvn' in requestData):
            payload["bvn"] = super(Card, self).encrypData(self.apiKey, requestData['bvn'])

        if('cardtype' in requestData):
            payload["cardtype"] = super(Card, self).encrypData(self.apiKey, requestData['cardtype']),

        return super(Card, self).sendRequest(Utils.cardChargeRoute, payload);


    def chargeWithToken(self, requestData):
        """Request to charge a card using a card token
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        customerID      -> Customer ID for tracking charge transaction
        narration       -> Transaction description
        cardtype        -> (Optional) Card type - Diamound
        '"""
        payload = {
            "merchantid": self.merchantKey,
            "amount": super(Card, self).encrypData(self.apiKey, requestData['amount']),
            "currency": super(Card, self).encrypData(self.apiKey, requestData['currency']),
            "custid": super(Card, self).encrypData(self.apiKey, requestData['customerID']),
            "narration": super(Card, self).encrypData(self.apiKey, requestData['narration']),
            "chargetoken": super(Card, self).encrypData(self.apiKey, requestData['cardToken'])
        }

        if('cardtype' in requestData):
            payload["cardtype"] = super(Card, self).encrypData(self.apiKey, requestData['cardtype']),

        return super(Card, self).sendRequest(Utils.cardChargeRoute, payload);


    def validate(self, requestData):
        """Request to validate a card charge transaction
        
        otp                      -> otp
        otpTransactionIdentifier -> Transaction reference from card charge request
        cardtype                 -> (Optional) Card type - Diamound
        '"""
        payload = {
            "merchantid": self.merchantKey,
            "otp": super(Card, self).encrypData(self.apiKey, requestData['otp']),
            "otptransactionidentifier": super(Card, self).encrypData(self.apiKey, requestData['otpTransactionIdentifier']),
        }

        if('cardtype' in requestData):
            payload["cardtype"] = super(Card, self).encrypData(self.apiKey, requestData['cardtype']),

        return super(Card, self).sendRequest(Utils.cardValidateRoute, payload);


    def preauth(self, requestData):
        """Request a PreAuthorization / Hold on a card for a specified amount
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        '"""
        payload = {
            "merchantid": self.merchantKey,
            "amount": super(Card, self).encrypData(self.apiKey, requestData['amount']),
            "currency": super(Card, self).encrypData(self.apiKey, requestData['currency']),
            "chargetoken": super(Card, self).encrypData(self.apiKey, requestData['cardToken'])
        }
        return super(Card, self).sendRequest(Utils.cardPreauthRoute, payload);


    def capture(self, requestData):
        """Request a Capture / Accept on a preauthorized amount on a card
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        transactionRef  -> Transaction reference from a preauthorize request
        authorizeID     -> Authorize ID from a preauthorize request
        '"""
        payload = {
            "merchantid": self.merchantKey,
            "amount": super(Card, self).encrypData(self.apiKey, requestData['amount']),
            "currency": super(Card, self).encrypData(self.apiKey, requestData['currency']),
            "trxreference": super(Card, self).encrypData(self.apiKey, requestData['transactionRef']),
            "trxauthorizeid": super(Card, self).encrypData(self.apiKey, requestData['authorizeID']),
        }

        return super(Card, self).sendRequest(Utils.cardCaptureRoute, payload);


    def refund(self, requestData):
        """Request a Refund on a charged card
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        transactionRef  -> Transaction reference from a preauthorize request
        authorizeID     -> Authorize ID from a preauthorize request
        '"""
        payload = {
            "merchantid": self.merchantKey,
            "amount": super(Card, self).encrypData(self.apiKey, requestData['amount']),
            "currency": super(Card, self).encrypData(self.apiKey, requestData['currency']),
            "trxreference": super(Card, self).encrypData(self.apiKey, requestData['transactionRef']),
            "trxauthorizeid": super(Card, self).encrypData(self.apiKey, requestData['authorizeID']),
        }
        return super(Card, self).sendRequest(Utils.cardRefundRoute, payload);


    def void(self, requestData):
        """Request a Refund on a charged card
        
        amount          -> Amount to debit from card
        cardToken       -> Token from a previously tokenized card
        currency        -> Transaction currency
        transactionRef  -> Transaction reference from a preauthorize request
        authorizeID     -> Authorize ID from a preauthorize request
        '"""
        payload = {
            "merchantid": self.merchantKey,
            "amount": super(Card, self).encrypData(self.apiKey, requestData['amount']),
            "currency": super(Card, self).encrypData(self.apiKey, requestData['currency']),
            "trxreference": super(Card, self).encrypData(self.apiKey, requestData['transactionRef']),
            "trxauthorizeid": super(Card, self).encrypData(self.apiKey, requestData['authorizeID']),
        }
        return super(Card, self).sendRequest(Utils.cardVoidRoute, payload);


