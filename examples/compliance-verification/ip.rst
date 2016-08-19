******************
IP
******************

::

    #
    # # IP CHECK
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    ipAddress = "41.58.202.50" # IP address to search
    country = "NGN"            # Country code (NGN)

    r = flw.ip.check(ipAddress, country)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data":{
    #         "responsecode":"00",
    #         "ipaddress":"41.58.202.50",
    #         "alpha2code":"NG",
    #         "alpha3code":"NGA",
    #         "responsemessage":"Completed Successfully",
    #         "countryname":"NIGERIA",
    #         "transactionreference":"FLW00293152"
    #     },
    #     "status":"success"
    # }