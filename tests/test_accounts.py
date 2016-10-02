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
    global transactionReference
    global otp
    global token
    global country
    global bankcode

    flw = Flutterwave("tk_NabYp2XjZ6G9WwdFruzK", "tk_tdyrSMQo8a", {"debug": True})

    ref = "{}{}".format("12345ref", time.time())[0:18]
    amount = "100"
    narration = "sample purchase"
    debitAccount = "0690000000"
    otp = "12345"
    country = "NG"
    bankcode = "044"


    # def test1AccountTokenize(self):
    #     print "\n---------###-- Flutterwave Account Tokenize --###------------"
    #     r = flw.account.tokenize(debitAccount, country)
    #     d = json.loads(r.text)

    #     global transactionReference
    #     transactionReference = d["data"]["transactionReference"]

    #     # self.assertEqual(d["data"]["responseCode"], "00")
    #     print "{}".format(r.text)
        

    # def test2AccountValidate(self):
    #     print "\n---------###-- Flutterwave Account Tokenize Validate --###------------"
    #     data = {
    #         "amount": amount,
    #         "ref": transactionReference,
    #         "otp": otp,
    #         "accountNumber": debitAccount,
    #         "narration": narration,
    #         "country": country
    #     }
    #     r = flw.account.validate(data)
    #     d = json.loads(r.text)

    #     global token
    #     token = d["data"]["accountToken"]
        
    #     # self.assertEqual(d["data"]["responsecode"], "00")
    #     print "{}".format(r.text)


    # def test3AccountCharge(self):
    #     print "\n---------###-- Flutterwave Account Charge --###------------"
    #     data = {
    #         "amount": amount,
    #         "token": token,
    #         "narration": narration,
    #         "country": country
    #     }

    #     r = flw.account.charge(data)
    #     d = json.loads(r.text)
        
    #     # self.assertEqual(d["data"]["responseCode"], "00")
    #     print "{}".format(r.text)


    # def test4AccountLookup(self):
    #     print "\n---------###-- Flutterwave Account Lookup --###------------"
    #     data = {
    #         "destBankCode": bankcode,
    #         "recipientAccount": debitAccount,
    #         "country": country
    #     }

    #     r = flw.account.lookup(data)
    #     d = json.loads(r.text)
        
    #     # self.assertEqual(d["data"]["responseCode"], "00")
    #     print "{}".format(r.text)


    def test5ChargeAny(self):
        print "\n---------###-- Flutterwave ChargeAny --###------------"
        data = {
            "narration": narration,
            "accountNumber": "0043480060",
            "bankCode": "058",
            "passcode":"123456789012",
            "amount": amount,
            "currency": "NGN",
            "firstName": "john",
            "lastName": "yemi",
            "email": "john.yemi@ggg.com",
            "transactionRef": "{}{}".format("12345ref", time.time())[0:18],
            "country": country
        }

        r = flw.account.chargeAny(data)
        d = json.loads(r.text)

        global transactionReference
        transactionReference = d["data"]["transactionreference"]
        
        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)


    def test6ValidateChargeAnyRef(self):
        print "\n---------###-- Flutterwave Validate ChargeAny --###------------"
        data = {
            "transactionRef": transactionReference,
            "otp": otp,
            "country": country
        }

        r = flw.account.validateChargeAnyRef(data)
        d = json.loads(r.text)
        
        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)


if __name__ == '__main__':
    unittest.main()