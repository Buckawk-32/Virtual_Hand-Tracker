import cv2
from Tracking import HandTrack

tracker = HandTrack()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
 
    frame1 = cv2.resize(frame, (640, 480))

    frame2 = cv2.flip(frame1, 1)

    tracker.findHand(frame2)
    tracker.startUI(frame2)
    

    cv2.imshow("Cam01", frame2)

    waitkey = cv2.waitKey(1)

    if waitkey == ord("q"):
        break