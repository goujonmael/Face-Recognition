import cv2

face_cascade=cv2.CascadeClassifier("./images/classifier/cascade.xml")
cap=cv2.VideoCapture('rtsp:192.168.1.113:8080/playlist.m3u')

while True:
    ret, frame=cap.read()
    frame = cv2.flip(frame, 1)
    tickmark=cv2.getTickCount()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=1 )
    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        cv2.putText(frame, "Mael", (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('video', frame)
cap.release()
cv2.destroyAllWindows()
