import requests
import base64
from Crypto.Cipher import DES3
from Crypto.Util import Counter
import hashlib


class Utils(object):
    """Flutterwave Utility Class provides common functionalities for extending classes"""

    # Service routes
    baseUrl = "http://staging1flutterwave.co:8080"

    ipCheckRoute = "/pwc/rest/fw/ipcheck/"
    binCheckRoute = "/pwc/rest/fw/check/"
    disburseSendRoute = "/pwc/rest/pay/send"

    bvnVerifyRoute = "/pwc/rest/bvn/verify/"
    bvnValidateRoute = "/pwc/rest/bvn/validate/"
    bvnResendOTPRoute = "/pwc/rest/bvn/resendotp/"

    accountTokenizeRoute = "/pwc/rest/recurrent/account"
    accountValidateRoute = "/pwc/rest/recurrent/account/validate"
    accountChargeRoute = "/pwc/rest/recurrent/account/charge"

    cardTokenizeRoute = "/pwc/rest/card/mvva/tokenize"
    cardChargeRoute = "/pwc/rest/card/mvva/pay"
    cardValidateRoute = "/pwc/rest/card/mvva/pay/validate"
    cardPreauthRoute = "/pwc/rest/card/mvva/preauthorize"
    cardCaptureRoute = "/pwc/rest/card/mvva/capture"
    cardRefundRoute = "/pwc/rest/card/mvva/refund"
    cardVoidRoute = "/pwc/rest/card/mvva/void"


    def encrypData(self, key, plainText):
        """Provides encryption for plaintext content required in request data."""

        md5Key = hashlib.md5(key.encode("utf-8")).digest()
        md5Key = "{}{}".format(md5Key, md5Key[0:8])

        blockSize = 8
        padDiff = blockSize - (len(plainText) % blockSize)
        cipher = DES3.new(md5Key, DES3.MODE_ECB)

        plainText = "{}{}".format(plainText, "".join(chr(padDiff) * padDiff))
        encrypted = base64.b64encode(cipher.encrypt(plainText))
        return encrypted
    

    def sendRequest(self, url, payload):
        """Request Handler forwards http request to flutterwave remote service"""
        # print payload
        r = requests.post("{}{}".format(self.baseUrl, url), json=payload, headers={})
        return r

