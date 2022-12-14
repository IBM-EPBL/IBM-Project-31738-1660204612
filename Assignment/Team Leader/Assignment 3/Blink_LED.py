import RPi.GPIO as GP
from time import sleep


GP.setwarnings(False)
GP.setmode(GP.BOARD)
GP.setup(8, GP.OUT, initial = GP.LOW)


while True:
    GP.output(8, GPIO.HIGH)
    print("The LED is ON")
    sleep(2)
    
    GP.output(8, GPIO.LOW)
    print("The LED is OFF")
    sleep(2)