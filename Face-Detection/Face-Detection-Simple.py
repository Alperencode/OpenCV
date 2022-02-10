import cv2 as cv
import numpy as np

# Using haarcascade and Starting Capture
face_cascade = cv.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Turning capture into gray pixels
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Using Face Detection Cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    
    for (x,y,w,h) in faces:
        
        # Numbers of x_start - y_start - x_end - y_end
        print(x, y, w, h)
        
        # The detected zones (Gray and colored)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # We are saving last image photo
        cv.imwrite("my_image.png", roi_color)
        
        # Rectange BGR, thickness, width and height
        color = (0, 0, 255)
        border = 2
        width = x + w
        height = y + h

        # Drawing rectangle
        if faces.all() == True:
            cv.rectangle(frame, (x, y), (width, height),color, border)

    # Display the result frame
    cv.imshow('frame', frame)

    if cv.waitKey(20) and 0xFF == ord('q'):
        break

cv.destroyAllWindows()