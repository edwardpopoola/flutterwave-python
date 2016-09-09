from flutterwave import Flutterwave
import time
import unittest
import json
import pprint

class TestDisburse(unittest.TestCase):

    global flw
    global amount
    global ref
    global relatedRef
    global bankCode
    global narration
    global debitAccount
    global creditAccount
    global recipientName
    global senderName
    global country
    global currency
    global accountToken
    global otpType1
    global otp1
    global otpType2
    global otp2

    flw = Flutterwave("tk_NabYp2XjZ6G9WwdFruzK", "tk_tdyrSMQo8a", {"debug": True})

    ref = "{}{}".format("12345ref", time.time())[0:18]
    amount = "100"
    bankCode = "058"
    narration = "sample disburse"
    debitAccount = "0690000000"
    creditAccount = "0921318712"
    recipientName = "test receiver"
    senderName = "test app"
    country = "NG"
    currency = "NGN"
    accountToken = ""
    otpType1 = "PHONE_OTP"
    otp1 = "12345"
    otpType2 = "ACCOUNT_DEBIT"
    otp2 = "1.00"



    def test1LinkAccount(self):
        print "\n---------###-- Flutterwave Link Account --###------------"

        r = flw.disburse.linkAccount(debitAccount, country)
        print "{}".format(r.text)
        d = json.loads(r.text)

        global relatedRef
        relatedRef = d["data"]["uniquereference"]

        self.assertEqual(d["data"]["responsecode"], "00")



    def test2ValidateLinkAccount(self):
        print "\n---------###-- Flutterwave Validate Link Account S1 --###------------"

        r = flw.disburse.validateLinkAccount(relatedRef, otpType1, otp1, country)
        print "{}".format(r.text)
        d = json.loads(r.text)

        self.assertEqual(d["data"]["responsecode"], "00")



    def test3ValidateLinkAccount(self):
        print "\n---------###-- Flutterwave Validate Link Account S2 --###------------"

        r = flw.disburse.validateLinkAccount(relatedRef, otpType2, otp2, country)
        print "{}".format(r.text)
        d = json.loads(r.text)

        global accountToken
        accountToken = d["data"]["accounttoken"]

        self.assertEqual(d["data"]["responsecode"], "00")



    def test4GetLinkedAccounts(self):
        print "\n---------###-- Flutterwave Get Linked Accounts --###------------"

        r = flw.disburse.getLinkedAccounts(country)
        print "{}".format(r.text)
        d = json.loads(r.text)

        self.assertEqual(d["data"]["responsecode"], "00")



    def test5DisburseSend(self):
        print "\n---------###-- Flutterwave Disburse send --###------------"
        data = {
            "amount": amount,
            "accountToken": accountToken,
            "ref": ref,
            "bankCode": bankCode,
            "narration": narration,
            "creditAccount": creditAccount,
            "recipientName": recipientName,
            "senderName": senderName,
            "country": country,
            "currency": currency
        }
        r = flw.disburse.send(data)
        print "{}".format(r.text)
        d = json.loads(r.text)

        self.assertEqual(d["data"]["responsecode"], "00")
        



if __name__ == '__main__':
    unittest.main()