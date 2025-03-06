import socket
# import RPi.GPIO as GPIO
import time

IP = '10.7.25.36'
PORT = 25565

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(11, GPIO.OUT)
# servo1 = GPIO.PWM(11, 50)  # Servo connected to pin11, set pulse to 50Hz.

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, PORT))
while True:

    data, addr = s.recvfrom(1024)  # Can receive text for maximum 1024 bits.

    # Display content.

    print("received message:{0} from PORT {1} on {2}".format(data.decode(), addr[1], addr[0]))
    # if data.decode() == 'left':
    #     MoveLeft = True
    # if data.decode() == 'right':
    #     MoveRight = True
    # if data.decode() == 'stop':
    #     Stop = True
    # if deta.decode() == 'fire':
    #     Fire = True
    #
    # while MoveLeft:
    #     # Code TBD
    #
    #     # angle = float(30)
    #     # servo1.ChangeDutyCycle(2 + (angle / 18))
    #     # time.sleep(0.5)
    #     # servo1.ChangeDutyCycle(0)
    #     # print('Rotation executed.')
    #
    # while MoveRight:
    #     # Code TBD
    #
    #     # angle = float(150)
    #     # servo1.ChangeDutyCycle(2 + (angle / 18))
    #     # time.sleep(0.5)
    #     # servo1.ChangeDutyCycle(0)
    #     # print('Rotation executed.')
    #
    # while Stop:
    #     # Code TBD
    #
    #     # servo1.stop()
    #
    # while Fire:
    #     # Code TBD
    #
    #
    if data.decode().lower() != 'bye':
        continue
    # GPIO.cleanup()
    break

s.close()
