import socket
import sys

IP = '192.168.1.185'
PORT = 25565

while True:
    msg = str(input('Input message:'))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(msg.encode(), (IP, PORT))
    s.close()

