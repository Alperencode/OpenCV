import cv2 as cv

face_cascade = cv.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')  # Using haarcascade
face_cascade2 = cv.CascadeClassifier('cascades/data/haarcascade_profileface.xml')  # Using haarcascade
# face_cascade3 = cv.CascadeClassifier('cascades/data/haarcascade_frontalcatface_extended.xml')  # Using haarcascade

cap = cv.VideoCapture(0)  # Starting Capture

while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # Turning capture into gray pixels
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)  # Using Face Detection Cascade
    faces2 = face_cascade2.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)  # Using Face Detection Cascade
    # faces3 = face_cascade3.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)  # Using Face Detection Cascade

    # FACE
    for (x,y,w,h) in faces:
        print(x, y, w, h)  # Its numbers of x_start - y_start - x_end - y_end
        roi_gray = gray[y:y+h, x:x+w]  # (ycord_start, ycord_end) & same thing for x
        roi_color = frame[y:y+h, x:x+w]  # for a colored capture
        img_item = "my_image.png"  # We will save the last face and this is file name for picture
        cv.imwrite(img_item, roi_gray)  # We are saving last image photo (Gray)
        color = (0, 0, 255)  # Rectangle BGR
        border = 2  # Rectangle border
        width = x + w  # Width
        height = y + h  # Height
        if faces.all() == True:
            cv.rectangle(frame, (x, y), (width, height),color, border)
            # cv.rectangle(CAPTURE, (X_Start, Y_Start), (X_End, Y_End), Rectangle BGR, Rectangle Border)

    # PROFILE FACE
    for (q, z, v, j) in faces2:
        print(q, z, v, j)  # Its numbers of x_start - y_start - x_end - y_end
        roi_gray = gray[z:z + j, q:q + v]  # (ycord_start, ycord_end) & same thing for x
        roi_color = frame[z:z + j, q:q + v]  # for a colored capture
        img_item = "my_image2.png"  # We will save the last face and this is file name for picture
        cv.imwrite(img_item, roi_gray)  # We are saving last image photo (Gray)
        color = (0, 0, 255)  # Rectangle BGR
        border = 2  # Rectangle border
        width2 = q + v  # Width
        height2 = z + j  # Height
        if faces2.all() == True:
            cv.rectangle(frame, (q, z), (width2, height2), color, border)
            # cv.rectangle(CAPTURE, (X_Start, Y_Start), (X_End, Y_End), Rectangle BGR, Rectangle Border)

    # CAT
    # for (q, z, v, j) in faces3:
        print(q, z, v, j)  # Its numbers of x_start - y_start - x_end - y_end
        roi_gray = gray[z:z + j, q:q + v]  # (ycord_start, ycord_end) & same thing for x
        roi_color = frame[z:z + j, q:q + v]  # for a colored capture
        img_item = "my_image2.png"  # We will save the last face and this is file name for picture
        cv.imwrite(img_item, roi_gray)  # We are saving last image photo (Gray)
        color = (0, 0, 255)  # Rectangle BGR
        border = 2  # Rectangle border
        width2 = q + v  # Width
        height2 = z + j  # Height
        # if faces3.all() == True:
        #    cv.rectangle(frame, (q, z), (width2, height2), color, border)
            # cv.rectangle(CAPTURE, (X_Start, Y_Start), (X_End, Y_End), Rectangle BGR, Rectangle Border)


    cv.imshow('frame', frame)  # Display the resulting frame
    # cv.imshow('gray', gray)  # Gray display (If you wanna show)
    if cv.waitKey(20) and 0xFF == ord('q'):
        break

# When everything done, release capture
cap.release()
cv.destroyAllWindows()  # This is not working and i don't know why