import requests
import base64
from Crypto.Cipher import DES3
from Crypto.Util import Counter
import hashlib


class Utils(object):
    """Flutterwave Utility Class provides common functionalities for extending classes"""


    def __init__(self, apiKey, merchantKey):
        # API credentials
        self.apiKey = apiKey
        self.merchantKey = merchantKey

        # BaseUrl
        self.baseUrl = "http://staging1flutterwave.co:8080"

        # Routes
        self.ipCheckRoute = "/pwc/rest/fw/ipcheck/"
        self.binCheckRoute = "/pwc/rest/fw/check/"
        self.disburseLinkAccountRoute = "/pwc/rest/pay/linkaccount"
        self.disburseValidateLinkAccountRoute = "/pwc/rest/pay/linkaccount/validate"
        self.disburseGetLinkedAccountRoute = "/pwc/rest/pay/getlinkedaccounts"
        self.disburseSendRoute = "/pwc/rest/pay/send"
        self.bvnVerifyRoute = "/pwc/rest/bvn/verify/"
        self.bvnValidateRoute = "/pwc/rest/bvn/validate/"
        self.bvnResendOTPRoute = "/pwc/rest/bvn/resendotp/"
        self.accountTokenizeRoute = "/pwc/rest/recurrent/account"
        self.accountValidateRoute = "/pwc/rest/recurrent/account/validate"
        self.accountChargeRoute = "/pwc/rest/recurrent/account/charge"
        self.accountLookupRoute = "/pwc/rest/pay/resolveaccount"
        self.accountChargeAnyRoute = "/pwc/rest/account/pay"
        self.accountValidateChargeAnyRefRoute = "/pwc/rest/account/pay/validate"
        self.accountValidateChargeAnyPhoneRoute = "/pwc/rest/accessbank/ussd/validate"
        self.cardTokenizeRoute = "/pwc/rest/card/mvva/tokenize"
        self.cardChargeRoute = "/pwc/rest/card/mvva/pay"
        self.cardChargeVerifyRoute = "/pwc/rest/card/mvva/status"
        self.cardValidateRoute = "/pwc/rest/card/mvva/pay/validate"
        self.cardPreauthRoute = "/pwc/rest/card/mvva/preauthorize"
        self.cardCaptureRoute = "/pwc/rest/card/mvva/capture"
        self.cardRefundRoute = "/pwc/rest/card/mvva/refund"
        self.cardVoidRoute = "/pwc/rest/card/mvva/void"
        self.cardBalanceroute = "/pwc/rest/card/mvva/cardenquiry"
        self.validateCardBalanceroute = "/pwc/rest/card/mvva/cardenquiry/validate"
        self.bankListRoute = "/pwc/rest/fw/banks/"
        self.achInstitutionsRoute = "/pwc/rest/card/mvva/institutions"
        self.achInstitutionRoute = "/pwc/rest/card/mvva/institutions/id"
        self.achAddUserRoute = "/pwc/rest/card/mvva/adduser"
        self.achChargeRoute = "/pwc/rest/card/mvva/chargeach"
        self.achWithdrawRoute = "/pwc/rest/card/mvva/withdraw"

        # State
        self.debug = False



    def setBaseUrl(self, url):
        self.baseUrl = url

    def enableDebug(self, enable):
        self.debug = enable


    def encryptData(self, plainText):
        """Provides encryption for plaintext content required in request data."""

        if(self.debug):
            print plainText

        md5Key = hashlib.md5(self.apiKey.encode("utf-8")).digest()
        md5Key = "{}{}".format(md5Key, md5Key[0:8])

        blockSize = 8
        padDiff = blockSize - (len(plainText) % blockSize)
        cipher = DES3.new(md5Key, DES3.MODE_ECB)

        plainText = "{}{}".format(plainText, "".join(chr(padDiff) * padDiff))
        encrypted = base64.b64encode(cipher.encrypt(plainText))
        return encrypted

    
    def decryptData(self, ciphertext):
        """Provides decryption for encrypted content returned from flutterwave service"""

        if(self.debug):
            print ciphertext

        md5Key = hashlib.md5(self.apiKey.encode("utf-8")).digest()
        md5Key = "{}{}".format(md5Key, md5Key[0:8])

        cipher = DES3.new(md5Key, DES3.MODE_ECB)

        decrypted = cipher.decrypt(base64.b64decode(ciphertext))
        return decrypted

        
    def sendRequest(self, url, payload):
        """Request Handler forwards http request to flutterwave remote service"""
        if(self.debug):
            print "{} :: {}{}".format(">>> URL", self.baseUrl, url)
            print "{} :: {}".format(">>> PAYLOAD",payload)

        r = requests.post("{}{}".format(self.baseUrl, url), json=payload, headers={})

        if(self.debug):
            print "{} :: {} - {}".format(">>> RESPONSE", r.status_code, r.text)

        return r


    def countryList(self):
        """Returns a List of Countries"""
        return {
            "NG": {
                "code": "NG",
                "name": "Nigeria"
            },
            "GH": {
                "code": "GH",
                "name": "Ghana"
            },
            "US": {
                "code": "US",
                "name": "United States"
            },
            "KE": {
                "code": "KE",
                "name": "Kenya"
            },
            "UK": {
                "code": "UK",
                "name": "United Kingdom"
            },
        }


    def currencyList(self):
        return {
            "NGN": {
                "code": "NGN",
                "name": "Naira"
            },
            "USD": {
                "code": "USD",
                "name": "US Dollar"
            },
            "GBP": {
                "code": "GBP",
                "name": "British Pound"
            },
            "EUR": {
                "code": "EUR",
                "name": "Euro"
            },
            "GHS": {
                "code": "GHS",
                "name": "Ghanian Cedi"
            },
            "KES": {
                "code": "KES",
                "name": "Kenya Shilling"
            },
        }

