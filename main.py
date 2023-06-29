from fastapi import FastAPI
import RPi.GPIO as GPIO
import time

servo_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # Using PWM frequency of 50Hz

# Function to control the servo motor
def control_servo(angle):
    duty_cycle = (angle / 18) + 2.5  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)

    


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/dooropen/")
def dooropen():
    pwm = GPIO.PWM(servo_pin, 50)
    control_servo(90)
    pwm.stop()
    return {"message": "Door is open"}

@app.get("/doorclosed/")
def doorclosed():
    pwm = GPIO.PWM(servo_pin, 50)
    control_servo(0)
    pwm.stop()
    return {"message": "Door is closed"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


#uvicorn main:app --host 2607:fea8:1f1c:6600::12 --port 8000 --reload
#uvicorn main:app --port 8000 --reload
#uvicorn main:app --host 0.0.0.0 --port 8000

'''
import requests

r = requests.get("http://[2607:fea8:1f1c:6600::12]:8000/")
print(r.text)
'''