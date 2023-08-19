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

'''
BLEService myService("a5d3a518-3d69-11ee-be56-0242ac120002");
BLEIntCharacteristic myCharacteristic("bd613920-3d64-11ee-be56-0242ac120002", BLERead | BLEBroadcast);

// Advertising parameters should have a global scope. Do NOT define them in 'setup' or in 'loop'
const uint8_t manufactData[4] = {0x01, 0x02, 0x03, 0x04};
const uint8_t serviceData[3] = {0x00, 0x01, 0x02};
// address is c0:49:ef:92:5e:66
'''