******************
ACH
******************

::

    #
    # # LIST ACH INSTITUTIONS
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    r = flw.ach.listInstitutions()
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data": {
    #         "institutions": [
    #             {
    #                 "credentials": {
    #                     "password": "Password",
    #                     "pin": null,
    #                     "username": "Online ID"
    #                 },
    #                 "name": "Bank of America",
    #                 "hasmfa": true,
    #                 "id": "5301a93ac140de84910000e0",
    #                 "type": "bofa",
    #                 "mfatypes": [
    #                     "code",
    #                     "list",
    #                     "questions(3)"
    #                 ]
    #             },
    #             .
    #             .
    #             .
    #         ],
    #         "responsecode": "00",
    #         "responsemessage": "Successful",
    #         "transactionreference": "FLWT00298038"
    #     },
    #     "status": "success"
    # }





    #
    # # GET SPECIFIC ACH INSTITUTION
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    institutionId = "5301a93ac140de84910000e0"   # Institution ID returned from Institutions list

    r = flw.ach.getInstitution()
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data": {
    #         "institutions": [
    #             {
    #                 "credentials": {
    #                     "password": "Password",
    #                     "pin": null,
    #                     "username": "Online ID"
    #                 },
    #                 "name": "Bank of America",
    #                 "hasmfa": true,
    #                 "id": "5301a93ac140de84910000e0",
    #                 "type": "bofa",
    #                 "mfatypes": [
    #                     "code",
    #                     "list",
    #                     "questions(3)"
    #                 ]
    #             }
    #         ],
    #         "responsecode": "00",
    #         "responsemessage": "Successful",
    #         "transactionreference": "FLWT00298040"
    #     },
    #     "status": "success"
    # }





    #
    # # ADD USER TO ACH INSTITUTION
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    data = {
        "username": institutionUsername,
        "password": institutionPassword,
        "pin": institutionPin,
        "email": email,
        "institutionType": institutionType,
        "country": country
    }

    r = flw.ach.getInstitution(data)
    print "{}".format(r.text)

    # RESPONSE
    #
    #
