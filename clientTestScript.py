from firestoreSnippet import *
import requests

deviceData = FindDevice("deviceId")
ipAddress = deviceData[0]["IPAddress"]

requests.get("http://" + ipAddress + ":8000/dooropen/")