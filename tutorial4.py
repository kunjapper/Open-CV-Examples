import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
    #width and height location will be at bottom right. origin is top left
    img = cv2.line(img, (0, height), (width, 0), (0,255,0), 5)
    img = cv2.rectangle(img, (100,100), (200, 200), (128,128,128), -1)
    #-1 will fill the box, 5 will be the line thickness
    img = cv2.circle(img, (500,500), 60, (0, 0, 255), 5)

    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, 'Anson made this', (200, height - 10), font, 2, (0,0,0), 5, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()