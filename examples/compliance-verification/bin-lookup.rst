******************
Card Bin
******************

::

    #
    # # CARD BIN LOOKUP
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    cardBin6 = "484250" # First 6-digits of card BIN
    country = "NG"     # Country code (NGN)

    r = flw.bin.check(cardBin6, country)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data":{
    #         "country":"MALAYSIA MY",
    #         "cardBin":"484250",
    #         "cardName":"VISA MAYBANK CREDIT",
    #         "transactionReference":"FLW00293139",
    #         "responseMessage":"Completed Successfully",
    #         "responseCode":"00"
    #     },
    #     "status":"success"
    # }