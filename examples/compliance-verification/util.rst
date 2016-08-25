******************
Utility
******************

::

    #
    # # BANK LIST
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    r = flw.bank.list()
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data": {
    #         "100": "SunTrust Bank",
    #         "214": "First City Monument Bank",
    #         "215": "Unity Bank",
    #         "221": "Stanbic IBTC Bank",
    #         "232": "Sterling Bank",
    #         "301": "JAIZ Bank",
    #         "302": "Eartholeum",
    #         "303": "ChamsMobile",
    #         "304": "Stanbic Mobile Money",
    #         "305": "Paycom",
    #         "306": "eTranzact",
    #         "307": "EcoMobile",
    #         "308": "FortisMobile",
    #         "309": "FBNMobile",
    #         "311": "ReadyCash (Parkway)",
    #         "313": "Mkudi",
    #         "314": "FET",
    #         "315": "GTMobile",
    #         "317": "Cellulant",
    #         "318": "Fidelity Mobile",
    #         "319": "TeasyMobile",
    #         "320": "VTNetworks",
    #         "322": "ZenithMobile",
    #         "323": "Access Money",
    #         "324": "Hedonmark",
    #         "325": "MoneyBox",
    #         "326": "Sterling Mobile",
    #         "327": "Pagatech",
    #         "328": "TagPay",
    #         "329": "PayAttitude Online",
    #         "401": "ASO Savings andamp; Loans",
    #         "402": "Jubilee Life Mortgage Bank",
    #         "403": "SafeTrust Mortgage Bank",
    #         "501": "Fortis Microfinance Bank",
    #         "523": "Trustbond",
    #         "526": "Parralex",
    #         "551": "Covenant Microfinance Bank",
    #         "552": "NPF MicroFinance Bank",
    #         "559": "Coronation Merchant Bank",
    #         "601": "FSDH",
    #         "990": "Test Bank",
    #         "999": "NIP Virtual Bank",
    #         "070": "Fidelity Bank",
    #         "030": "Heritage",
    #         "076": "Skye Bank",
    #         "032": "Union Bank",
    #         "033": "United Bank for Africa",
    #         "035": "Wema Bank",
    #         "082": "Keystone Bank",
    #         "084": "Enterprise Bank",
    #         "044": "Access Bank",
    #         "050": "Ecobank Plc",
    #         "011": "First Bank of Nigeria",
    #         "057": "Zenith Bank",
    #         "058": "GTBank Plc",
    #         "063": "Diamond Bank",
    #         "023": "CitiBank",
    #         "068": "Standard Chartered Bank"
    #     },
    #     "status": "success"
    # }




    #
    # # ENCRYPT / DECRYPT
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    print ">>> Plain"
    plain = "I got encrypted, then reversed."

    encrypted = flw.util.encryptData(plain)

    print ">>> Encrypted"

    decrypted = flw.util.decryptData(encrypted)

    print ">>> Decrypted"
    print decrypted

    # RESPONSE
    # >>> Plain
    # I got encrypted, then reversed.
    # >>> Encrypted
    # K0yxLI7nA9wrAomi1klHvxRObHchZbeSKdVGW+fTZs0=
    # >>> Decrypted
    # I got encrypted, then reversed.




    #
    # # CURRENCY LIST
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    print flw.util.currencyList()

    # RESPONSE
    # {
    #     'USD': {'code': 'USD', 'name': 'US Dollar'},
    #     'GHS': {'code': 'GHS', 'name': 'Ghanian Cedi'},
    #     'NGN': {'code': 'NGN', 'name': 'Naira'},
    #     'GBP': {'code': 'GBP', 'name': 'British Pound'},
    #     'KES': {'code': 'KES', 'name': 'Kenya Shilling'},
    #     'EUR': {'code': 'EUR', 'name': 'Euro'}
    # }




    #
    # # COUNTRY LIST
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    print flw.util.countryList()

    # RESPONSE
    # {
    #     'UK': {'code': 'UK', 'name': 'United Kingdom'}, 
    #     'GH': {'code': 'GH', 'name': 'Ghana'}, 
    #     'KE': {'code': 'KE', 'name': 'Kenya'}, 
    #     'US': {'code': 'US', 'name': 'United States'}, 
    #     'NG': {'code': 'NG', 'name': 'Nigeria'}
    # }