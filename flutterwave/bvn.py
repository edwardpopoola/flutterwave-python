from utils import Utils

class Bvn(Utils):
    """Flutterwave BVN module

        Provides methods for verifying a users BVN.
    """

    def __init__(self, util):
        self.util = util
        
        
    
    def verify(self, userBvn, verifyUsing, country):
        """Request verification for a users BVN
        
        UserBvn     -> the users 11-digit BVN to verify
        verifyUsing -> verification method to use - Voice, SMS
        country     -> Country code (NGN)
        '"""
        payload = {
            "otpoption": self.util.encryptData(verifyUsing),
            "merchantid": self.util.merchantKey,
            "bvn": self.util.encryptData(userBvn),
            "country": self.util.encryptData(country)
        }
        return self.util.sendRequest(self.util.bvnVerifyRoute, payload);

    
    def validate(self, userBvn, otp, transactionReference, country):
        """Request validation for a users BVN
        
        userBvn              -> the users 11-digit BVN to validate
        otp                  -> otp received by user from verify request
        transactionreference -> refernce received from previous verify request
        country              -> Country code (NGN)
        '"""
        payload = {
            "otp": self.util.encryptData(otp),
            "transactionreference": self.util.encryptData(transactionReference),
            "merchantid": self.util.merchantKey,
            "bvn": self.util.encryptData(userBvn),
            "country": self.util.encryptData(country)
        }
        return self.util.sendRequest(self.util.bvnValidateRoute, payload);


    def resendOtp(self, verifyUsing, transactionReference, country):
        """Resend OTP for BVN verification
        
        verifyUsing          -> verification method to use - Voice, SMS
        transactionreference -> refernce received from previous verify request
        country              -> Country code (NGN)
        '"""
        payload = {
            "validateoption": self.util.encryptData(verifyUsing),
            "merchantid": self.util.merchantKey,
            "transactionreference": self.util.encryptData(transactionReference),
            "country": self.util.encryptData(country)
        }
        return self.util.sendRequest(self.util.bvnResendOTPRoute, payload);

