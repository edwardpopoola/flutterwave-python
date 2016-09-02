from utils import Utils

class Ach(Utils):
    """Flutterwave Automated Clearing House class
    """

    def __init__(self, util):
        self.util = util


    def listInstitutions(self, country):
        """Request a list of ACH Institutions
        
        country       -> Country code (NG)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "country": self.util.encryptData(country)
        }
        return self.util.sendRequest(self.util.achInstitutionsRoute, payload);


    def getInstitution(self, institutionId, country):
        """Request details for a specific ACH Institution

        institutionId -> Institution ID returned from Institutions list
        country       -> Country code (NG)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "institutionid": self.util.encryptData(institutionId),
            "country": self.util.encryptData(country)
        }
        return self.util.sendRequest(self.util.achInstitutionRoute, payload);


    def getUserTransactions(self, requestData):
        """Request to add a user to an ACH Institution
        Returns users Accounts and Transactions

        requestData.username          -> Institution username returned from institution detail - credentials
        requestData.password          -> Institution password returned from institution detail - credentials
        requestData.pin               -> Institution pin returned from institution detail - credentials
        requestData.email             -> New User email
        requestData.institutionType   -> Institution Type returned from Institution detail
        requestData.country           -> Country code (NG)
        '"""
        payload = {
            "merchantid": self.util.merchantKey,
            "username": self.util.encryptData(requestData['username']),
            "password": self.util.encryptData(requestData['password']),
            "email": self.util.encryptData(requestData['email']),
            "institution": self.util.encryptData(requestData['institutionType']),
            "country": self.util.encryptData(requestData['country'])
        }

        if('pin' in requestData):
            payload["pin"] = self.util.encryptData(requestData['pin']),

        return self.util.sendRequest(self.util.achAddUserRoute, payload);
        