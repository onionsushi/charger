import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid
from datetime import datetime
import socket
# Use a service account.
cred = credentials.Certificate("cred.json")


app = firebase_admin.initialize_app(cred, )

db = firestore.client()

#Three data base collection 
#1. Transaction
#2. Device
#3. User







def AddData(CollectionName : str, data : dict, DocumentName: str = ""):
    if not DocumentName:
        DocumentName = uuid.uuid4()

    doc_ref = db.collection(CollectionName).document(str(DocumentName))
    doc_ref.set(data)


def FindData(CollectionName : str, arg1, relation, arg2):
#   
    result = []
    docs = db.collection(CollectionName).where(arg1, relation, arg2).stream()
    for doc in docs:
        print("FindData: " + str(doc.to_dict()))
        result.append(doc.to_dict())
    return result

def GetConfiguration():
    result = []
    ref = db.collection("Configuration").document("Master")
    docs = ref.stream()
    for doc in docs:
        result.append(doc.to_dict())
    if len(result) > 0 :
        return result[0]
    else:
        return None
    

def SetConfiguration(data: dict):
    ref = db.collection("Configuration").document("Master")
    ref.update(data)

def AddUser(userName: str):
    userId = uuid.uuid4()
    userdata = {
    "UserId": str(userId),
    "UserName": userName,
    "Status" : "Off",
    "Balance" : 0,
    }
    AddData("UserData", userdata, userId)
    return str(userId)

def FindUser(UserId: str):
    return FindData("UserData", "UserId", "==", UserId)

def ModifyUserData(userId: str, data: dict):
    ref = db.collection("UserData").document(userId)
    ref.update(data)
    print("ModifyUserData: " + str(FindUser(userId)))

def FindDevice(deviceId: str):
    return FindData("DeviceData", "deviceId", "==", deviceId)

def AddDevice(deviceId: str, ipaddress: str ):
    deviceData = {
    "deviceId": deviceId,
    "Status" : "Off",
    "Balance" : 0,
    "CurrentUser": None,
    "IPAddress": ipaddress,
    "recentUse": None,
    }
    AddData("DeviceData", deviceData, deviceId)

def StartCharge(deviceId, userId):
    ref = db.collection("DeviceData").document(deviceId)
    ref.update({"recentUse": datetime.now(), "Status": "On", "CurrentUser": userId})
    
def finishCharge(deviceId):
    ref = db.collection("DeviceData").document(deviceId)
    ref.update({"recentUse": datetime.now(), "Status": "Off", "Balance": 0, "CurrentUser": None})

def setConfigure(deviceId, ipaddress):
    if FindDevice(deviceId) == []:
        AddDevice(deviceId, ipaddress)
    else: 
        ref = db.collection("DeviceData").document(deviceId)
        ref.update({"recentUse": datetime.now(), "IPAddress": ipaddress, "Status" : "Off", "CurrentUser": None, "recentUse": datetime.now()})

def changeStatus(deviceId, status:bool):
    ref = db.collection("SamDeviceData").document(deviceId)
    ref.update({"recentUse": datetime.now()})
    if status:
        ref.update({"Status": "On"})
    else:
        ref.update({"Status": "Off"})

def CheckStatus(deviceId):
    status = FindData("DeviceData", "deviceId", "==", deviceId)
    return status

def BalanceChange(UserId: str, amount : int):
    res = FindUser(UserId)
    if res != []:

        currentBalance = res[0]["Balance"]
        if (currentBalance - amount > 0):
            ModifyUserData(UserId, {"Balance" : currentBalance - amount})
            return True
        else:
            return False
        
if __name__ == "__main__":
    #Add device
    AddDevice("deviceId", "sampleipaddress")
    #add user
    userId = AddUser("TestUser")
    #change device ipaddress
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)#ipv4
    ipaddress = socket.getaddrinfo(hostname, None, socket.AF_INET6)[0][4][0] #ipv6
    setConfigure("deviceId", ipaddress)
    # #Add balance to test user
    # ModifyUserData(userId, {"Balance": 2000})
    # #start charging
    # StartCharge("deviceId", userId)
    # BalanceChange(userId, 1000)
    # finishCharge("deviceId")