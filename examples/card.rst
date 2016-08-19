******************
Card
******************


    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})
    
    data = {
        "validateOption": "SMS",          # verification method to use - Voice, SMS
        "authModel": "BVN",               # authentication Model - BVN, PIN, NOAUTH
        "cardNumber": "4842508225502547", # Card Number
        "cvv": "136",                     # Card CVV
        "expiryMonth": "10",              # Card expiry month
        "expiryYear": "18",               # Card expiry year
        "bvn": "12345678901",             # (Optional) User BVN, required only for authModel=BVN
        "country": "NGN"                  # Country code (NGN)
    }
    
    r = flw.card.tokenize(data)
    print "{}".format(r.text)
    
    
    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"02",
    #         "responsemessage":"Pending BVN Validation",
    #         "otptransactionidentifier":"FLW00293082",
    #         "transactionreference":"FLW00293082",
    #         "responsehtml":null,
    #         "responsetoken":null
    #     },
    #     "status":"success"
    # }
    
    
    
    
    
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})
    
    data = {
        "otp": "12345",                            # otp
        "otpTransactionIdentifier": "FLW00293082", # Transaction reference from card charge / tokenize request
        "country": "NGN"                           # Country code (NGN)
    }
    
    r = flw.card.validate(data)
    print "{}".format(r.text)
    
    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"00",
    #         "responsemessage":"Approved",
    #         "otptransactionidentifier":null,
    #         "transactionreference":null,
    #         "responsehtml":null,
    #         "responsetoken":"3IQROMOLDW0b3jp1082"
    #     },
    #     "status":"success"
    # }
    
    
    
    
    
    
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})
    
    data = {
        "amount": "100",                           # Amount to debit from card
        "authModel": "BVN",                        # authentication Model - BVN, PIN, NOAUTH, VBVSECURECODE
        "cardNumber": "4842508225502547",          # Card Number
        "cvv": "136",                              # Card CVV
        "expiryMonth": "10",                       # Card expiry month
        "expiryYear": "18",                        # Card expiry year
        "bvn": "12345678901",                      # (Optional) User BVN, required only for authModel=BVN
        "currency": "NGN",                         # Transaction currency
        "customerID": "cust1471629671",            # Customer ID for tracking charge transaction
        "narration": "sample card purchase",       # Transaction description
        "responseUrl": "http://your_callback_url", # Callback Url
        "currency": "NGN",                         # Transaction currency
        "country": "NGN"                           # Country code (NGN)
    }
    
    r = flw.card.charge(data)
    print "{}".format(r.text)
    
    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"02",
    #         "responsemessage":"Pending BVN Validation",
    #         "otptransactionidentifier":"FLW00293084",
    #         "transactionreference":"FLW00293084",
    #         "responsehtml":null,
    #         "responsetoken":null
    #     },
    #     "status":"success"
    # }
    
    
    
    
    
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})
    
    data = {
        "amount": "100",                     # Amount to debit from card
        "cardToken": "3IQROMOLDW0b3jp1082",  # Token from a previously tokenized card
        "customerID": "cust1471629671",      # Customer ID for tracking charge transaction
        "narration": "sample card purchase", # Transaction description
        "currency": "NGN",                   # Transaction currency
        "country": "NGN"                     # Country code (NGN)
    }
    
    r = flw.card.chargeWithToken(data)
    print "{}".format(r.text)
    
    # RESPONSE
    
    
    
    
    
    
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})
    
    data = {
        "amount": "100",                    # Amount to debit from card
        "currency": "NGN",                  # Transaction currency
        "cardToken": "3IQROMOLDW0b3jp1082", # Token from a previously tokenized card
        "country": "NGN"                    # Country code (NGN)
    }
    
    r = flw.card.preauth(data)
    print "{}".format(r.text)
    
    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"0",
    #         "authorizeId":"1471629598383",
    #         "responsemessage":"Successful",
    #         "otptransactionidentifier":null,
    #         "transactionreference":"FLW00293091",
    #         "responsehtml":null,
    #         "responsetoken":null
    #     },
    #     "status":"success"
    # }
    
    
    
    
    
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})
    
    data = {
        "amount": "100",                 # Amount to debit from card
        "currency": "NGN",               # Transaction currency
        "transactionRef": "FLW00293091", # Transaction reference from a preauthorize request
        "authorizeID": "1471629598383",  # Authorize ID from a preauthorize request
        "country": "NGN"                 # Country code (NGN)
    }
    
    r = flw.card.capture(data)
    print "{}".format(r.text)
    
    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"0",
    #         "authorizeId":"",
    #         "responsemessage":"Successful",
    #         "otptransactionidentifier":null,
    #         "transactionreference":"FLW00293092",
    #         "responsehtml":null,
    #         "responsetoken":null
    #     },
    #     "status":"success"
    # }
    
    
    
    
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})
    
    data = {
        "amount": "100",                 # Amount to debit from card
        "currency": "NGN",               # Transaction currency
        "transactionRef": "FLW00293091", # Transaction reference from a preauthorize request
        "authorizeID": "1471629598383",  # Authorize ID from a preauthorize request
        "country": "NGN"                 # Country code (NGN)
    }
    
    r = flw.card.void(data)
    print "{}".format(r.text)
    
    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"0",
    #         "authorizeId":"",
    #         "responsemessage":"Successful",
    #         "otptransactionidentifier":null,
    #         "transactionreference":"FLW00293092",
    #         "responsehtml":null,
    #         "responsetoken":null
    #     },
    #     "status":"success"
    # }
    
    
    
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})
    
    data = {
        "amount": "100",                 # Amount to debit from card
        "currency": "NGN",               # Transaction currency
        "transactionRef": "FLW00293091", # Transaction reference from a preauthorize request
        "authorizeID": "1471629598383",  # Authorize ID from a preauthorize request
        "country": "NGN"                 # Country code (NGN)
    }
    
    r = flw.card.refund(data)
    print "{}".format(r.text)
    
    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"0",
    #         "authorizeId":"",
    #         "responsemessage":"Successful",
    #         "otptransactionidentifier":null,
    #         "transactionreference":"FLW00293092",
    #         "responsehtml":null,
    #         "responsetoken":null
    #     },
    #     "status":"success"
    # }
