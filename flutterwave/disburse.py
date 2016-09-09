from utils import Utils

class Disburse(Utils):
    """Flutterwave Disburse module

        Provides methods for running transactions between accounts
    """

    def __init__(self, util):
        self.util = util


    def linkAccount(self, accountNumber, country):
        """Request to link an account for disbursement.

        accountNumber -> Account number to be linked as disbursement source
        country       -> Country code (NGN)
        """

        payload = {
            "merchantid": self.util.merchantKey,
            "accountnumber": self.util.encryptData(accountNumber),
            "country": self.util.encryptData(country)
        }
        return self.util.sendRequest(self.util.disburseLinkAccountRoute, payload);



    def validateLinkAccount(self, relatedRef, otpType, otp, country):
        """Request a disburse to a destination account.

        relatedReference -> Unique reference returned from the linkAccount request
        otpType          -> OTP Method in Use (ACCOUNT_DEBIT | PHONE_OTP)
        otp              -> User otp
        country          -> Country code (NGN)
        """

        payload = {
            "merchantid": self.util.merchantKey,
            "relatedreference": self.util.encryptData(relatedRef),
            "otp": self.util.encryptData(otp),
            "otptype": self.util.encryptData(otpType),
            "country": self.util.encryptData(country)
        }
        return self.util.sendRequest(self.util.disburseValidateLinkAccountRoute, payload);



    def getLinkedAccounts(self, country):
        """Returned your linked Accounts
        """

        payload = {
            "merchantid": self.util.merchantKey,
            "country": self.util.encryptData(country)
        }
        return self.util.sendRequest(self.util.disburseGetLinkedAccountRoute, payload);
    


    def send(self, requestData):
        """Request a disburse to a destination account.
        
        amount        -> Amount to credit recipient (1000.00)
        accounttoken  -> Dissburse Source Account token from linked Account
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
            "accounttoken": self.util.encryptData(requestData['accountToken']),
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
