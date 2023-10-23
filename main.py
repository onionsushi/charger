from fastapi import FastAPI, BackgroundTasks
import time
import subprocess
import bluetoothControl 
import uvicorn


# Function to control the servo motor

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/locktoggle/")
async def locktoggle(background_tasks : BackgroundTasks):
    subprocess.call('sudo sh gatt.sh', shell=True)
    # background_tasks.add_task(bluetoothControl.discover_and_write, bluetoothControl.service_uuid, bluetoothControl.characteristic_uuid, b'\x04')
    return {"message": "Lock toggled"}


#write a function that run a sleep function for 3 seconds in fast api background

#uvicorn main:app --host 2607:fea8:1f1c:6600::12 --port 8000 --reload
#uvicorn main:app --port 8000 --reload
#uvicorn main:app --host 0.0.0.0 --port 8000

'''
import requests

r = requests.get("http://[2607:fea8:1f1c:6600::12]:8000/")
print(r.text)
'''
if __name__ == "__main__":
    uvicorn.run(app, host="10.0.0.176", port=8000)
    