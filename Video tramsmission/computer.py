import cv2
import numpy
import socket
import struct
import os
import time

address = [0, 0]
HOST = '192.168.43.201'
PORT = 2079
buffSize = 90732
count = 0


if not os.path.exists('pics'):
    os.makedirs('pics')


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print('now waiting for frames...')

while True:

    key = cv2.waitKey(1) & 0xFF

    data, address = server.recvfrom(buffSize)

    if len(data) == 1 and data[0] == 1:
        server.close()
        cv2.destroyAllWindows()
        exit()

    if len(data) != 4:
        length = 0
    else:
        length = struct.unpack('i', data)[0]
    data, address = server.recvfrom(buffSize)

    if length != len(data):
        continue
    data = numpy.array(bytearray(data))
    imgdecode = cv2.imdecode(data, 1)
    count += 1
    filename = 'pics/' + 'vid_' + time.strftime('%Y%m%d-%H%M%S') + '_' + str(count) + '.jpg'
    cv2.imwrite(filename, imgdecode)
    print('have received one frame')
    cv2.imshow('frames', imgdecode)

    if key == ord('q'):
        print('End transmission')
        break

server.close()
cv2.destroyAllWindows()
