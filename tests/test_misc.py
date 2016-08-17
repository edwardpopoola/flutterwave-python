from flutterwave import Flutterwave
import time
import unittest
import json
import pprint

class TestMisc(unittest.TestCase):

    global flw
    global ip
    global cardBin6

    flw = Flutterwave("tk_NabYp2XjZ6G9WwdFruzK", "tk_tdyrSMQo8a")

    ref = "{}{}".format("12345ref", time.time())
    ip = "127.0.0.1"
    cardBin6 = "484250"


    def test1Ip(self):
        print "\n---------###-- Flutterwave IP Check --###------------"
        r = flw.ip.check(ip)
        d = json.loads(r.text)

        self.assertEqual(d["data"]["responsecode"], "00")
        print "{}".format(r.text)


    def test2Bin(self):
        print "\n---------###-- Flutterwave Card BIN Check --###------------"
        r = flw.bin.check(cardBin6)
        d = json.loads(r.text)

        self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)
        



if __name__ == '__main__':
    unittest.main()