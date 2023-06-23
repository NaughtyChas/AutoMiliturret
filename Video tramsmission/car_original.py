import cv2
import socket
import struct
# import numpy
# import time


broke = False
count = 0
HOST = '10.7.30.16'
PORT = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.connect((HOST, PORT))
print('start sending frames...')
capture = cv2.VideoCapture(0)

try:
    while True:
        success, frame = capture.read()
        count = count + 1
        while not success and frame is None:
            success, frame = capture.read()
        cv2.imshow('VideoFeed (Press q to exit)', frame)
        result, imgencode = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
        server.sendall(struct.pack('i', imgencode.shape[0]))
        server.sendall(imgencode)
        print('sent ' + str(count) + ' frames')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            broke = True
            break


except Exception as e:
    print(e)
    server.sendall(struct.pack('s', b'Error'))
    capture.release()
    server.close()

finally:
    if broke:
        print('Transmission interrupted')
    else:
        print('Transmission completed')

    capture.release()
    server.close()
