
from flutterwave import Flutterwave
import time
import unittest
import json
import pprint

class TestAch(unittest.TestCase):

    global flw
    global institutionId
    global institutionUsername
    global institutionPassword
    global institutionPin
    global institutionType
    global country
    global email

    flw = Flutterwave("tk_NabYp2XjZ6G9WwdFruzK", "tk_tdyrSMQo8a", {"debug": True})

    institutionId = ""
    country = "NG"
    email = "abc@xyz.com"
    institutionPin = "1"
    institutionType = "wells"
    institutionPassword = "plaid_good"
    institutionUsername = "plaid_test"




    def test1List(self):
        print "\n---------###-- Flutterwave ACH List Institutions --###------------"

        r = flw.ach.listInstitutions(country)
        d = json.loads(r.text)

        global institutionId
        institutionId = d["data"]["institutions"][0]['id']
        global institutionUsername
        #institutionUsername = d["data"]["institutions"][0]['credentials']['username']
        global institutionPassword
        #institutionPassword = d["data"]["institutions"][0]['credentials']['password']
        global institutionPin
        #institutionPin = d["data"]["institutions"][0]['credentials']['pin']
        global institutionType
        #institutionType = d["data"]["institutions"][0]['type']

        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)


    def test2Detail(self):
        print "\n---------###-- Flutterwave ACH Get Institution --###------------"
        r = flw.ach.getInstitution(institutionId, country)
        d = json.loads(r.text)

        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)

    
    def test3AddUser(self):
        print "\n---------###-- Flutterwave ACH Add User --###------------"

        payload = {
            "username": institutionUsername,
            "password": institutionPassword,
            "email": email,
            "institutionType": institutionType,
            "country": country
        }

        r = flw.ach.addUser(payload)
        d = json.loads(r.text)

        # self.assertEqual(d["data"]["responseCode"], "00")
        print "{}".format(r.text)





if __name__ == '__main__':
    unittest.main()