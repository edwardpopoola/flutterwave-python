from utils import Utils

class Bvn(Utils):
    """Flutterwave BVN module

        Provides methods for verifying a users BVN.
    """

    def __init__(self, apiKey, merchantKey):
        self.apiKey = apiKey
        self.merchantKey = merchantKey

    
    def verify(self, userBvn, verifyUsing):
        """Request verification for a users BVN
        
        UserBvn     -> the users 11-digit BVN to verify
        verifyUsing -> verification method to use - Voice, SMS
        '"""
        payload = {
            "otpoption": super(Bvn, self).encrypData(self.apiKey, verifyUsing),
            "merchantid": self.merchantKey,
            "bvn": super(Bvn, self).encrypData(self.apiKey, userBvn)
        }
        return super(Bvn, self).sendRequest(Utils.bvnVerifyRoute, payload);

    
    def validate(self, userBvn, otp, transactionReference):
        """Request validation for a users BVN
        
        userBvn              -> the users 11-digit BVN to validate
        otp                  -> otp received by user from verify request
        transactionreference -> refernce received from previous verify request
        '"""
        payload = {
            "otp": super(Bvn, self).encrypData(self.apiKey, otp),
            "transactionreference": super(Bvn, self).encrypData(self.apiKey, transactionReference),
            "merchantid": self.merchantKey,
            "bvn": super(Bvn, self).encrypData(self.apiKey, userBvn),
        }
        return super(Bvn, self).sendRequest(Utils.bvnValidateRoute, payload);


    def resendOtp(self, verifyUsing, transactionReference):
        """Resend OTP for BVN verification
        
        verifyUsing          -> verification method to use - Voice, SMS
        transactionreference -> refernce received from previous verify request
        '"""
        payload = {
            "validateoption": super(Bvn, self).encrypData(self.apiKey, verifyUsing),
            "merchantid": self.merchantKey,
            "transactionreference": super(Bvn, self).encrypData(self.apiKey, transactionReference),
        }
        return super(Bvn, self).sendRequest(Utils.bvnResendOTPRoute, payload);

