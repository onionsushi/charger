import firestoreSnippet
import requests
import socket
dburl = "sampleurl.com"

class Charger():
    deviceId: str
    owner: str
    currentUser: str| None
    balance: int
    WattPerMin: int
    price: int
    currency: str

    def Register(self):
        headers = {"content-type" : "application/json",
                   "Accept" : "*/*"}
        data = {
            "deviceId": self.deviceId,
            "ipAddress" : socket.gethostbyname(socket.gethostname())
        }
        requests.post(dburl + "/device/register", headers = headers, data =  data)

    
    def checkClient(self, userId: str):
        res = firestoreSnippet.FindData("Sample Data", "userId", "==", userId)
        if res != []:
            if res.get("balance", 0) > 0:
                self.currentUser = userId
                self.balance = res[""]
            else:
                print("Not enough balance")
        else:
            print("Unable to retrieve client info")
    
    def setPrice(self, newPrice, newCurrency = ""):
        if not newCurrency:
            price = newPrice

    def UpdateClinentBalance(self, userId, amount):
        res = firestoreSnippet.FindData("Sample Data", "userId", "==", userId)
    