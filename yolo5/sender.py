import socket
import sys

IP = '10.7.25.36'
PORT = 25565

while True:
    msg = str(input('Input message:'))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(msg.encode(), (IP, PORT))
    s.close()

