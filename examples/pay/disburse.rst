******************
Disburse
******************

::


    #
    # # LINK ACCOUNT
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    debitAccount = "0690000000"  # Account number to be linked as disbursement source
    country = "NG"               # Country code (NG)

    r = flw.disburse.linkAccount(debitAccount, country)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"02",
    #         "responsemessage":"Pending Validation",
    #         "uniquereference":"FLWT00302622"
    #     },
    #     "status":"success"
    # }




    #
    # # VALIDATE LINK ACCOUNT - STAGE 1
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    relatedRef = "FLWT00302622"  # Unique reference returned from the linkAccount request
    otpType = "PHONE_OTP"        # OTP Method in Use (ACCOUNT_DEBIT | PHONE_OTP) - BOTH Required
    otp = "12345"                # User otp
    country = "NG"               # Country code (NG)

    r = flw.disburse.validateLinkAccount(relatedRef, otpType, otp, country)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"02",
    #         "responsemessage":"Pending Validation",
    #         "uniquereference":"FLWT00302882",
    #         "accounttoken":null
    #     },
    #     "status":"success"
    # }




    #
    # # VALIDATE LINK ACCOUNT - STAGE 2
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    relatedRef = "FLWT00302622"  # Unique reference returned from the linkAccount request
    otpType = "ACCOUNT_DEBIT"    # OTP Method in Use (ACCOUNT_DEBIT | PHONE_OTP)
    otp = "1.00"                 # User otp
    country = "NG"               # Country code (NG)

    r = flw.disburse.validateLinkAccount(relatedRef, otpType, otp, country)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"00",
    #         "responsemessage":"Account successfully validated and linked",
    #         "uniquereference":"FLWT00302882",
    #         "accounttoken":"UdLqD1Y7XA08In19810"
    #     },
    #     "status":"success"
    # }




    #
    # # LIST LINKED ACCOUNTS
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    country = "NG"  # Country code (NG)

    r = flw.disburse.getLinkedAccounts(country)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data": {
    #         "responsecode": "00",
    #         "linkedaccounts": [
    #             {
    #                 "accountnumber": "0690000005",
    #                 "added": "2016-09-05 03:46:08.0",
    #                 "status": "VALIDATED"
    #             },
    #             {
    #                 "accountnumber": "0690000003",
    #                 "added": "2016-09-06 12:29:04.0",
    #                 "status": "VALIDATED"
    #             },
    #             .
    #             .
    #             .
    #         ],
    #         "responsemessage": "Successful",
    #         "uniquereference": "FLWT00302625"
    #     },
    #     "status": "success"
    # }




    #
    # # DISBURSE TO ACCOUNT
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    data = {
        "amount": "100",                  # Amount to credit recipient (1000.00)
        "accountToken": "-xxxxxxx-",      # Dissburse Source Account token from linked Account
        "ref": "12345ref1471634145",      # A transaction reference you will provide for tracking
        "bankCode": "058",                # Recipients Bankcode
        "narration": "sample disburse",   # Description to include in the transaction
        "creditAccount": "0921318712",    # Account to credit
        "recipientName": "test receiver", # Transaction recipient name
        "senderName": "test app",         # Transaction sender name
        "country": "NG",                  # Country code (NG)
        "currency": "NGN"                 # Transaction Currency
    }
    r = flw.disburse.send(data)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"00",
    #         "responsemessage":"Completed Successfully",
    #         "uniquereference":"12345ref1471634145"
    #     },
    #     "status":"success"
    # }