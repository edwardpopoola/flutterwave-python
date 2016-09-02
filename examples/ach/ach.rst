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
    # # GET ACH USER ACCOUNTS & TRANSACTIONS
    #
    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    data = {
        "username": institutionUsername,
        "password": institutionPassword,
        "email": email,
        "institutionType": institutionType,
        "country": country
    }

    r = flw.ach.getUserTransactions(data)
    print "{}".format(r.text)

    # RESPONSE
    # {
    #     "data": {
    #         "responsecode": "00",
    #         "responsemessage": "Successful",
    #         "transactionreference": "FLWT00298245",
    #         "accounts": [
    #               {
    #                   "item": null,
    #                   "balance": {
    #                       "current": 1274.93,
    #                       "available": 1203.42
    #                   },
    #                   "subtype": "savings",
    #                   "meta": {
    #                       "number": "9606",
    #                       "limit": null,
    #                       "name": "Plaid Savings"
    #                   },
    #                   "numbers": null,
    #                   "institutionType": null,
    #                   "id": null,
    #                   "type": "depository",
    #                   "user": null
    #               },
    #               .
    #               .
    #               .
    #           ],
    #         "transactions": [
    #               {
    #                   "date": {
    #                       "year": 2014,
    #                       "dayOfYear": 202,
    #                       "weekyear": 2014,
    #                       "values": [
    #                           2014,
    #                           7,
    #                           21
    #                       ],
    #                       "chronology": {
    #                           "zone": {
    #                               "fixed": true,
    #                               "id": "UTC"
    #                           }
    #                       },
    #                       "weekOfWeekyear": 30,
    #                       "monthOfYear": 7,
    #                       "dayOfWeek": 1,
    #                       "era": 1,
    #                       "dayOfMonth": 21,
    #                       "yearOfCentury": 14,
    #                       "fieldTypes": [
    #                           {
    #                               "rangeDurationType": null,
    #                               "name": "year",
    #                               "durationType": {
    #                                   "name": "years"
    #                               }
    #                           },
    #                           {
    #                               "rangeDurationType": {
    #                                   "name": "years"
    #                               },
    #                               "name": "monthOfYear",
    #                               "durationType": {
    #                                   "name": "months"
    #                               }
    #                           },
    #                           {
    #                               "rangeDurationType": {
    #                                   "name": "months"
    #                               },
    #                               "name": "dayOfMonth",
    #                               "durationType": {
    #                                   "name": "days"
    #                               }
    #                           }
    #                       ],
    #                       "centuryOfEra": 20,
    #                       "yearOfEra": 2014,
    #                       "fields": [
    #                           {
    #                               "minimumValue": -292275054,
    #                               "leapDurationField": {
    #                                   "name": "days",
    #                                   "precise": true,
    #                                   "unitMillis": 86400000,
    #                                   "type": {
    #                                       "name": "days"
    #                                   },
    #                                   "supported": true
    #                               },
    #                               "name": "year",
    #                               "durationField": {
    #                                   "name": "years",
    #                                   "precise": false,
    #                                   "unitMillis": 31556952000,
    #                                   "type": {
    #                                       "name": "years"
    #                                   },
    #                                   "supported": true
    #                               },
    #                               "rangeDurationField": null,
    #                               "type": {
    #                                   "rangeDurationType": null,
    #                                   "name": "year",
    #                                   "durationType": {
    #                                       "name": "years"
    #                                   }
    #                               },
    #                               "unitMillis": null,
    #                               "maximumValue": 292278993,
    #                               "lenient": false,
    #                               "supported": true
    #                           },
    #                           {
    #                               "minimumValue": 1,
    #                               "leapDurationField": {
    #                                   "name": "days",
    #                                   "precise": true,
    #                                   "unitMillis": 86400000,
    #                                   "type": {
    #                                       "name": "days"
    #                                   },
    #                                   "supported": true
    #                               },
    #                               "name": "monthOfYear",
    #                               "durationField": {
    #                                   "name": "months",
    #                                   "precise": false,
    #                                   "unitMillis": 2629746000,
    #                                   "type": {
    #                                       "name": "months"
    #                                   },
    #                                   "supported": true
    #                               },
    #                               "rangeDurationField": {
    #                                   "name": "years",
    #                                   "precise": false,
    #                                   "unitMillis": 31556952000,
    #                                   "type": {
    #                                       "name": "years"
    #                                   },
    #                                   "supported": true
    #                               },
    #                               "type": {
    #                                   "rangeDurationType": {
    #                                       "name": "years"
    #                                   },
    #                                   "name": "monthOfYear",
    #                                   "durationType": {
    #                                       "name": "months"
    #                                   }
    #                               },
    #                               "unitMillis": null,
    #                               "maximumValue": 12,
    #                               "lenient": false,
    #                               "supported": true
    #                           },
    #                           {
    #                               "minimumValue": 1,
    #                               "leapDurationField": null,
    #                               "name": "dayOfMonth",
    #                               "durationField": {
    #                                   "name": "days",
    #                                   "precise": true,
    #                                   "unitMillis": 86400000,
    #                                   "type": {
    #                                       "name": "days"
    #                                   },
    #                                   "supported": true
    #                               },
    #                               "rangeDurationField": {
    #                                   "name": "months",
    #                                   "precise": false,
    #                                   "unitMillis": 2629746000,
    #                                   "type": {
    #                                       "name": "months"
    #                                   },
    #                                   "supported": true
    #                               },
    #                               "type": {
    #                                   "rangeDurationType": {
    #                                       "name": "months"
    #                                   },
    #                                   "name": "dayOfMonth",
    #                                   "durationType": {
    #                                       "name": "days"
    #                                   }
    #                               },
    #                               "unitMillis": 86400000,
    #                               "maximumValue": 31,
    #                               "lenient": false,
    #                               "supported": true
    #                           }
    #                       ]
    #                   },
    #                   "amount": 200,
    #                   "pending": false,
    #                   "entityId": null,
    #                   "type": {
    #                       "primary": "special"
    #                   },
    #                   "accountId": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
    #                   "score": {
    #                       "detail": null,
    #                       "master": null
    #                   },
    #                   "meta": {
    #                       "contact": null,
    #                       "ids": null,
    #                       "location": {
    #                           "zip": null,
    #                           "address": null,
    #                           "city": "San Francisco",
    #                           "coordinates": null,
    #                           "state": "CA"
    #                       }
    #                   },
    #                   "name": "ATM Withdrawal",
    #                   "id": "0AZ0De04KqsreDgVwM1RSRYjyd8yXxSDQ8Zxn",
    #                   "pendingTransactionId": null,
    #                   "category": [
    #                       "Transfer",
    #                       "Withdrawal",
    #                       "ATM"
    #                   ],
    #                   "categoryId": "21012002"
    #               },
    #               .
    #               .
    #           ]
    #     },
    #     "status": "success"
    # }
