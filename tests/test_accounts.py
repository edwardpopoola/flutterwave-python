from flutterwave import Flutterwave
import time
import unittest
import json
import pprint

class TestAccounts(unittest.TestCase):

    global flw
    global ref
    global amount
    global narration
    global debitAccount
    global creditAccount
    global otp
    global token

    flw = Flutterwave("tk_NabYp2XjZ6G9WwdFruzK", "tk_tdyrSMQo8a")

    ref = "{}{}".format("12345ref", time.time())
    amount = "100"
    narration = "sample purchase"
    debitAccount = "0695149079"
    creditAccount = "0690000020"
    otp = "12345"


    def test1AccountTokenize(self):
        print "\n---------###-- Flutterwave Account Tokenize --###------------"
        r = flw.account.tokenize(debitAccount)
        d = json.loads(r.text)

        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)
        

    def test2AccountValidate(self):
        print "\n---------###-- Flutterwave Account Tokenize Validate --###------------"
        data = {
            "amount": amount,
            "ref": ref,
            "otp": otp,
            "accountNumber": debitAccount,
            "narration": narration
        }
        r = flw.account.validate(data)
        d = json.loads(r.text)
        
        # self.assertEqual(d["data"]["responsecode"], "00")
        print "{}".format(r.text)


    def test3AccountCharge(self):
        print "\n---------###-- Flutterwave Account Charge --###------------"
        data = {
            "amount": amount,
            "token": ref,
            "narration": narration
        }

        r = flw.account.charge(data)
        d = json.loads(r.text)
        
        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)


if __name__ == '__main__':
    unittest.main()