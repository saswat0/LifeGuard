import cvlib as cv
from object_detection import draw_bbox
import cv2
import time
import numpy as np

webcam = cv2.VideoCapture(0)

t0 = time.time()

centre0 = np.zeros(2)
isDrowning = False

while webcam.isOpened():

    _, frame = webcam.read()

    bbox, label, conf = cv.detect_common_objects(frame)

    if(len(bbox) > 0):
        bbox0 = bbox[0]
        centre = [0, 0]

        centre = [(bbox0[0]+bbox0[2])/2, (bbox0[1]+bbox0[3])/2]

        hmov = abs(centre[0]-centre0[0])
        vmov = abs(centre[1]-centre0[1])

        x = time.time()

        threshold = 10

        if(hmov > threshold or vmov > threshold):
            print(x-t0, 's')
            t0 = time.time()
            isDrowning = False
        else:
            print(x-t0, 's')
            if((time.time() - t0) > 10):
                isDrowning = True

        # print('bbox: ', bbox, 'centre:', centre, 'centre0:', centre0)
        print('Drowning Status: ', isDrowning)

        centre0 = centre

    out = draw_bbox(frame, bbox, label, conf, isDrowning)
    cv2.imshow("Real-time object detection", out)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
