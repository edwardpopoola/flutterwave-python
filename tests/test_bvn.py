from flutterwave import Flutterwave
import time
import unittest
import json
import pprint

class TestBvn(unittest.TestCase):

    global flw
    global bvn
    global verifyUsing
    global otp
    global transactionReference
    global country


    flw = Flutterwave("tk_NabYp2XjZ6G9WwdFruzK", "tk_tdyrSMQo8a")

    verifyUsing = "SMS"
    bvn = "12345678901"
    otp = "12345"
    country = "NGN"





    def test1Bvn(self):
        print "\n---------###-- Flutterwave BVN verify --###------------"
        r = flw.bvn.verify(bvn, verifyUsing, country)
        d = json.loads(r.text)

        global transactionReference
        transactionReference = d["data"]["transactionReference"]

        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)


    def test2ResendOtp(self):
        print "\n---------###-- Flutterwave BVN resendotp --###------------"
        r = flw.bvn.resendOtp(verifyUsing, transactionReference, country)
        d = json.loads(r.text)

        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)

    
    def test3BvnValidate(self):
        print "\n---------###-- Flutterwave BVN validate --###------------"
        r = flw.bvn.validate(bvn, otp, transactionReference, country)
        d = json.loads(r.text)

        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)


if __name__ == '__main__':
    unittest.main()