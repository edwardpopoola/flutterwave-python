from flutterwave import Flutterwave
import unittest

print Flutterwave
test = Flutterwave("tk_NabYp2XjZ6G9WwdFruzK", "tk_tdyrSMQo8a")
print test


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


# 
def testip(ip):
    r = test.ip.check(ip)
    print "{} {}".format(r.status_code, r.text, r.json)

# "484250"
def testBin(cardBin):
    r = test.bin.check(cardBin)
    print "{} {}".format(r.status_code, r.text, r.json)

# "22171877153", "SMS"
def testbvn(bvn, verifyUsing):
    r = test.bvn.verify(bvn, verifyUsing)
    print "{} {}".format(r.status_code, r.text, r.json)

# "22171877153", "46014", "FLW00291068"
def testbvnValidate(userBvn, otp, transactionReference):
    r = test.bvn.validate(userBvn, otp, transactionReference)
    print "{} {}".format(r.status_code, r.text, r.json)

# "Voice", "FLW00291069"
def testresendOtp(verifyUsing, transactionReference):
    r = test.bvn.resendOtp(verifyUsing, transactionReference)
    print "{} {}".format(r.status_code, r.text, r.json)

# "0704580684", "100", "0706329119", "ref2", "sample description"
def testaccountCharge(debitAccount, amount, creditAccount, ref, narration):
    data = {
        "debitAccount": debitAccount,
        "amount": amount,
        "creditAccount": creditAccount,
        "ref": ref,
        "narration": narration
    }
    r = test.account.charge(data)
    print "{} {}".format(r.status_code, r.text, r.json)

# "100", "51449", "ref2", "RiXvyUVIlL0SToO0492"
def testvalidateAccountCharge(amount, otp, ref, token):
    data = {
        "amount": amount,
        "ref": ref,
        "otp": otp,
        "accountToken": token
    }
    r = test.account.validateCharge(data)
    print "{} {}".format(r.status_code, r.text, r.json)

# "ref3", "3"
def testAccountResendOtp(validationOption, ref):
    data = {
        "ref": ref,
        "validateOption": validationOption
    }
    r = test.account.resendOTP(data)
    print "{} {}".format(r.status_code, r.text, r.json)


# "100", "ref2", "058", "sample disburse", "0921318712", "obinna", "private-app", "NG", "NGN"
def testDisburseSend(amount, ref, bankCode, narration, creditAccount, recipientName, senderName, country, currency):
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
    r = test.disburse.send(data)
    print "{} {}".format(r.status_code, r.text, r.json)

# "SMS","BVN", "4842508225502547", "136", "10", "18", "22171877153"
def testCardTokenize(validateOption, authModel, cardNumber, cvv, expiryMonth, expiryYear, bvn):
    data = {
        "validateOption": validateOption,
        "authModel": authModel,
        "cardNumber": cardNumber,
        "cvv": cvv,
        "expiryMonth": expiryMonth,
        "expiryYear": expiryYear,
        "bvn": bvn,
    }

    r = test.card.tokenize(data)
    print "{} {}".format(r.status_code, r.text, r.json)

# "100","BVN", "4842508225502547", "136", "10", "18", "NGN", "cust1", "sample card charge", "", "", "22171877153"
def testCardCharge(amount, authModel, cardNumber, cvv, expiryMonth, expiryYear, currency, customerID, narration, responseUrl, cardtype, bvn):
    data = {
        "amount": amount,
        "authModel": authModel,
        "cardNumber": cardNumber,
        "cvv": cvv,
        "expiryMonth": expiryMonth,
        "expiryYear": expiryYear,
        "bvn": bvn,
        "currency": currency,
        "customerID": customerID,
        "narration": narration,
        "responseUrl": responseUrl,
        "currency": currency
    }

    r = test.card.charge(data)
    print "{} {}".format(r.status_code, r.text, r.json)

# "100", "BRRMQt53gf0804h9866", "NGN", "cust1", "sample card token charge", "", ""
def testChargeWithToken(amount, cardToken, currency, customerID, narration, cardtype, responseUrl):
    data = {
        "amount": amount,
        "cardToken": cardToken,
        "currency": currency,
        "customerID": customerID,
        "narration": narration,
        "responseUrl": responseUrl,
        "currency": currency
    }

    r = test.card.chargeWithToken(data)
    print "{} {}".format(r.status_code, r.text, r.json)

# "78717", "FLW00291276"
def testCardValidate(otp, otpTransactionIdentifier):
    data = {
        "otp": otp,
        "otpTransactionIdentifier": otpTransactionIdentifier
    }

    r = test.card.validate(data)
    print "{} {}".format(r.status_code, r.text, r.json)


def testCardPreauth(amount, currency, cardToken):
    data = {
        "amount": amount,
        "currency": currency,
        "cardToken": cardToken,
    }

    r = test.card.preauth(data)
    print "{} {}".format(r.status_code, r.text, r.json)


def testCardCapture(amount, currency, transactionRef, authorizeID):
    data = {
        "amount": amount,
        "currency": currency,
        "transactionRef": transactionRef,
        "authorizeID": authorizeID
    }

    r = test.card.capture(data)
    print "{} {}".format(r.status_code, r.text, r.json)


def testCardVoid(amount, currency, transactionRef, authorizeID):
    data = {
        "amount": amount,
        "currency": currency,
        "transactionRef": transactionRef,
        "authorizeID": authorizeID
    }

    r = test.card.void(data)
    print "{} {}".format(r.status_code, r.text, r.json)

def testCardRefund(amount, currency, transactionRef, authorizeID):
    data = {
        "amount": amount,
        "currency": currency,
        "transactionRef": transactionRef,
        "authorizeID": authorizeID
    }

    r = test.card.refund(data)
    print "{} {}".format(r.status_code, r.text, r.json)








