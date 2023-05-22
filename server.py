from fastapi import FastAPI


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid
from datetime import datetime
import firestoreSnippet
# Use a service account.
cred = credentials.Certificate("sampledb-385301-firebase-adminsdk-mk65f-309efd2f1b.json")


app = firebase_admin.initialize_app(cred, )

db = firestoreSnippet.client()


app = FastAPI()
# Register device. If the device is already registered, refresh ipaddress
@app.post("/device/register/{deviceID}")
def read_status(body: dict):
    deviceID = body["deviceID"]
    ipAddress = body["ipAddress"]
    res = firestoreSnippet.setConfigure(deviceId=deviceID, ipaddress=ipAddress)
    return res


# Check current status of device (call from devices)
@app.get("/device/{deviceID}")
def read_status(deviceID: str):
    res = firestoreSnippet.CheckStatus(deviceId=deviceID)
    return res

#modify user data (for current device)
@app.post("/user/load/{UserID}")
def read_item(userId: str, body: dict):
    # userdata = {
    #     "userName" : userName,
    #     "email": emailaddress,
    #     "currentDevice": None,
    #     "balance": 0
    # }
    res = firestoreSnippet.ModifyUserData(userId, body)
    return {"status": res.get("Status")}

#update status 
@app.post("/update/{deviceID}")
def update(deviceID: str):
    res = firestoreSnippet.CheckStatus(deviceId=deviceID)
    return {"status": res.get("Status")}
