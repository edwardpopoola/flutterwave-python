******************
Flutterwave Python
******************

Python Bindings for the Flutterwave Payment APIs.

==================
Installation
==================

To install the flutterwave python package, run the command below::

    pip install --upgrade flutterwave

or::

    easy_install --upgrade flutterwave

See http://www.pip-installer.org/en/latest/index.html for instructions
on installing pip. If you are on a system with easy_install but not
pip, you can use easy_install instead.

To install from source, run::

    python setup.py install

=================
API Services
=================
- Charge Accounts
- Charge Cards
- Disburse to Accounts
- BVN Validation
- Card BIN Lookup
- IP Check

===================
Getting Started
===================

To debit an account, two steps: first, tokenize the account, then charge account using the returned token::

    from flutterwave import Flutterwave
    flw = Flutterwave("<api_key>", "<merchant_key>", {"debug": True})

    payload = {
        "token": "FZeDswE6ju0ONCL3864",    # Token returned from account tokenization request
        "amount": "100",    # Amount to debit from account
        "narration": "payment for coffee",     # Description for this payment
        "country": "NGN"     # country of debit source
    }

    r = flw.account.charge(payload)
    print "{}".format(r.text)

    # Response
    # {
    #   {
    #       "transactionreference":"FLW00292801",
    #       "responseMessage":"Approved or Completed Successfully",
    #       "responseCode":"00"
    #   },
    #   "status":"success"
    # }




Tokens are valid means of charging an account or card subsequently. 

Sign up at http://flutterwave.com for API keys.

============
Testing
============

Flutterwave-Python is written in python version 2.7 and can be tested by running the command below from the package folder::

    python -m unittest discover