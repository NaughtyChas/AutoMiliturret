import time
import cv2
import socket
import struct
import os

# import numpy


broke = False
count = 0
photo_count = 0
video_recording = False

HOST = '10.7.30.16'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.connect((HOST, PORT))
print('start sending frames...')
capture = cv2.VideoCapture(0)

if not os.path.exists('pics'):
    os.makedirs('pics')
if not os.path.exists('video'):
    os.makedirs('video')


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
        if count % 10 == 0:
            print('sent ' + str(count) + ' frames')

        key = cv2.waitKey(1) & 0xFF

        if key == ord('o'):
            photo_success, photo_frame = capture.read()
            if photo_success:
                photo_count += 1
                photo_result, photo_imgencode = cv2.imencode('.jpg', photo_frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                filename = 'pics/' + 'pic_' + time.strftime('%Y%m%d-%H%M%S') + '_' + str(count) + '.jpg'
                with open(filename, 'wb') as f:
                    f.write(photo_imgencode)

                server.sendall(struct.pack('i', photo_imgencode.shape[0]))
                server.sendall(photo_imgencode)
                print('[Status]  Photo sent')
        elif key == ord('p'):
            video_recording = not video_recording

            if video_recording:
                count = 0
                print('[Status]  Start recording...')
            else:
                print('[Status]  Stop recording')

        if video_recording:
            video_result, video_imgencode = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
            filename = 'video/' + 'vid_' + time.strftime('%Y%m%d-%H%M%S') + '_' + str(count) + '.jpg'
            with open(filename, 'wb') as f:
                f.write(video_imgencode)

            server.sendall(struct.pack('i', video_imgencode.shape[0]))
            server.sendall(video_imgencode)

        if key == ord('q'):
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
