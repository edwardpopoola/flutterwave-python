from flutterwave import Flutterwave
import time
import unittest
import json
import pprint

class TestMisc(unittest.TestCase):

    global flw
    global ip
    global cardBin6
    global country

    flw = Flutterwave("tk_NabYp2XjZ6G9WwdFruzK", "tk_tdyrSMQo8a", {"debug": True})

    ref = "{}{}".format("12345ref", time.time())[0:18]
    ip = "41.58.202.50"
    cardBin6 = "484250"
    country = "NG"


    def test1Ip(self):
        print "\n---------###-- Flutterwave IP Check --###------------"
        r = flw.ip.check(ip, country)
        d = json.loads(r.text)

        self.assertEqual(d["data"]["responsecode"], "00")
        print "{}".format(r.text)


    def test2Bin(self):
        print "\n---------###-- Flutterwave Card BIN Check --###------------"
        r = flw.bin.check(cardBin6, country)
        d = json.loads(r.text)

        self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)

    def test2Bin(self):
        print "\n---------###-- Flutterwave Get Bank List --###------------"
        r = flw.bank.list()
        d = json.loads(r.text)

        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)

    def testEncryptDecrypt(self):
        print "\n---------###-- Utilities : Encrypt and Decrypt --###------------"
        print ">>> Plain"
        plain = "I got encrypted, then reversed."
        encrypted = flw.util.encryptData(plain)
        print ">>> Encrypted"
        decrypted = flw.util.decryptData(encrypted)
        print ">>> Decrypted"
        print decrypted
        



if __name__ == '__main__':
    unittest.main()