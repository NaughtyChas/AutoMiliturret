import cv2
import numpy
import socket
import struct
import time

HOST = '10.7.30.16'
PORT = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.connect((HOST, PORT))
print('start sending frames...')
capture = cv2.VideoCapture(0)
ret, frame = capture.read()
cv2.imshow('Video feed', frame)

try:
    while True:
        success, frame = capture.read()
        while not success and frame is None:
            success, frame = capture.read()
    result, imgencode = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
    server.sendall(struct.pack('i', imgencode.shape[0]))
    server.sendall(imgencode)
    print('single frame sent')
except Exception as e:
    print(e)
    server.sendall(struct.pack('c', 1))
    capture.release()
    server.close()

