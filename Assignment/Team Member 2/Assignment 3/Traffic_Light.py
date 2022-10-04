from gpiozero import LED
from time import sleep


red = LED(17)
yellow = LED(22)
green = LED(27)


while True:
    red.on()
    print("Red light is ON")
    for i in range(100, 0, -1):
        print("Remaining time: ",i)
        sleep(1)
    red.off()

    yellow.on()
    print("Yellow light is ON")
    for i in range(5, 0, -1):
        print("Remaining time: ",i)
        sleep(1)
    yellow.off()

    green.on()
    print("Green light is ON")
    for i in range(30, 0, -1):
        print("Remaining time: ",i)
        sleep(1)
    green.off()