******************
Disburse
******************

::

    #
    # # DISBURSE TO ACCOUNT
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    data = {
        "amount": "100",                  # Amount to credit recipient (1000.00)
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