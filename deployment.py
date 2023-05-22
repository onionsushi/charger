import os
import requests
import firestoreSnippet

response = requests.get("https://api.ipify.org/?format=json")
ipAddress = response.json()["ip"]
data = {"ipAddress" : ipAddress}
firestoreSnippet.SetConfiguration(data)


os.system("uvicorn main:app --host " + "0.0.0.0" +" --port 8000 --reload")