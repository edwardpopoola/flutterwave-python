******************
BVN
******************

::

    #
    # # VERIFY BVN
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    bvn = "12345678901" # the users 11-digit BVN to validate
    verifyUsing = "SMS" # verification method to use - Voice, SMS
    country = "NG"     # Country code (NG)

    r = flw.bvn.verify(bvn, verifyUsing, country)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data":{
    #         "transactionReference":"FLW00293154",
    #         "responseMessage":"Successful, pending OTP validation",
    #         "responseCode":"00"
    #     },
    #     "status":"success"
    # }





    #
    # # RESEND BVN OTP
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    verifyUsing = "SMS"                  # verification method to use - Voice, SMS
    transactionReference = "FLW00293154" # refernce received from previous verify request
    country = "NG"                      # Country code (NG)

    r = flw.bvn.resendOtp(verifyUsing, transactionReference, country)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"00",
    #         "responsemessage":"Successful, pending OTP validation"
    #     },
    #     "status":"success"
    # }




    #
    # # VALIDATE BVN VERIFY
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    bvn = "12345678901"                  # the users 11-digit BVN to validate
    otp = "12345"                        # otp received by user from verify request
    transactionReference = "FLW00293154" # refernce received from previous verify request
    country = "NG"                      # Country code (NG)

    r = flw.bvn.validate(bvn, otp, transactionReference, country)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data":{
    #         "firstName":"NICK",
    #         "lastName":"BILL",
    #         "imageBase64":"-",
    #         "phoneNumber":"07069703016",
    #         "enrollmentBranch":"-",
    #         "registrationDate":"06-JUL-15",
    #         "enrollmentBank":"044",
    #         "dateOfBirth":"13-JUN-92",
    #         "middleName":"SHAWN",
    #         "bvn":"12345678901",
    #         "responseMessage":"Completed Successfully",
    #         "responseCode":"00"
    #     },
    #     "status":"success"
    # }