# Install RPi.GPIO First
# sudo apt-get update
# sudo apt-get -y install python-rpi.gpio

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)  # Servo connected to pin11, set pulse to 50Hz.
servo1.start(0)

try:
    while True:
        angle = float(input('Enter angle between 0 and 180: '))
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

finally:
    servo1.stop()
    GPIO.cleanup()
    print("Rotation executed.")
