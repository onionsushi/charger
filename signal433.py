import time
import RPi.GPIO as GPIO

# GPIO pin number for the transmitter
def sendLockSignal():
    transmitter_pin = 17
# Set up the GPIO pin for output
    GPIO.setmode(GPIO.BCM)	
    GPIO.setup(transmitter_pin, GPIO.OUT)
    for i in range(3):
        GPIO.output(transmitter_pin, GPIO.HIGH)
        print("high")
        time.sleep(0.1)
        GPIO.output(transmitter_pin, GPIO.LOW)
        print("low")
        time.sleep(0.1)
    # Clean up GPIO resources
    GPIO.cleanup()
    print("Done")
