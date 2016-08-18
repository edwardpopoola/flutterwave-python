from flutterwave import Flutterwave
import time
import unittest
import json
import pprint

class TestDisburse(unittest.TestCase):

    global flw
    global amount
    global ref
    global bankCode
    global narration
    global creditAccount
    global recipientName
    global senderName
    global country
    global currency

    flw = Flutterwave("tk_NabYp2XjZ6G9WwdFruzK", "tk_tdyrSMQo8a", {"debug": True})

    ref = "{}{}".format("12345ref", time.time())[0:18]
    amount = "100"
    bankCode = "058"
    narration = "sample disburse"
    creditAccount = "0921318712"
    recipientName = "test receiver"
    senderName = "test app"
    country = "NG"
    currency = "NGN"


    def test1DisburseSend(self):
        print "\n---------###-- Flutterwave Disburse send --###------------"
        data = {
            "amount": amount,
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