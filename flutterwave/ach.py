from utils import Utils

class Ach(Utils):
    """Flutterwave Automated Clearing House class
    """

    def __init__(self, util):
        self.util = util



        # self.achInstitutionsRoute = "/pwc/rest/card/mvva/institutions"
        # self.achInstitutionRoute = "/pwc/rest/card/mvva/institutions/id"
        # self.achAddUserRoute = "/pwc/rest/card/mvva/adduser"
        # self.achChargeRoute = "/pwc/rest/card/mvva/chargeach"
        # self.achWithdrawRoute = "/pwc/rest/card/mvva/withdraw"

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


    def addUser(self, requestData):
        """Request to add a user to an ACH Institution

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
            "pin": self.util.encryptData(requestData['pin']),
            "email": self.util.encryptData(requestData['email']),
            "institution": self.util.encryptData(requestData['institutionType']),
            "country": self.util.encryptData(requestData['country'])
        }
        return self.util.sendRequest(self.util.achAddUserRoute, payload);


    
    def charge(self, requestData):
        """Request a charge as a user from an ACH Institution

        country                  -> Country code (NG)
        '"""


    def withdraw(self, requestData):
        """Request a withdraw as a user from an ACH Institution

        country                  -> Country code (NG)
        '"""
