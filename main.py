from fastapi import FastAPI
import RPi.GPIO as GPIO
import time
from signal433 import sendLockSignal


# Function to control the servo motor

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/doorclosed/")
def doorclosed():
    sendLockSignal()
    return {"message": "Door is closed"}


#uvicorn main:app --host 2607:fea8:1f1c:6600::12 --port 8000 --reload
#uvicorn main:app --port 8000 --reload
#uvicorn main:app --host 0.0.0.0 --port 8000

'''
import requests

r = requests.get("http://[2607:fea8:1f1c:6600::12]:8000/")
print(r.text)
'''