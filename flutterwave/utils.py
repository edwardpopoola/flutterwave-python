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
        self.disburseSendRoute = "/pwc/rest/pay/send"
        self.bvnVerifyRoute = "/pwc/rest/bvn/verify/"
        self.bvnValidateRoute = "/pwc/rest/bvn/validate/"
        self.bvnResendOTPRoute = "/pwc/rest/bvn/resendotp/"
        self.accountTokenizeRoute = "/pwc/rest/recurrent/account"
        self.accountValidateRoute = "/pwc/rest/recurrent/account/validate"
        self.accountChargeRoute = "/pwc/rest/recurrent/account/charge"
        self.cardTokenizeRoute = "/pwc/rest/card/mvva/tokenize"
        self.cardChargeRoute = "/pwc/rest/card/mvva/pay"
        self.cardValidateRoute = "/pwc/rest/card/mvva/pay/validate"
        self.cardPreauthRoute = "/pwc/rest/card/mvva/preauthorize"
        self.cardCaptureRoute = "/pwc/rest/card/mvva/capture"
        self.cardRefundRoute = "/pwc/rest/card/mvva/refund"
        self.cardVoidRoute = "/pwc/rest/card/mvva/void"
        self.bankListRoute = "/pwc/rest/fw/banks/"

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
    

    def sendRequest(self, url, payload):
        """Request Handler forwards http request to flutterwave remote service"""
        if(self.debug):
            print "{} :: {}{}".format(">>> URL", self.baseUrl, url)
            print "{} :: {}".format(">>> PAYLOAD",payload)

        r = requests.post("{}{}".format(self.baseUrl, url), json=payload, headers={})

        if(self.debug):
            print "{} :: {} - {}".format(">>> RESPONSE", r.status_code, r.text)

        return r

