import cv2 as cv

# Using haarcascade
face_cascade = cv.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')  

# Using haarcascade
face_cascade2 = cv.CascadeClassifier('cascades/data/haarcascade_profileface.xml')  

# Using haarcascade
# face_cascade3 = cv.CascadeClassifier('cascades/data/haarcascade_frontalcatface_extended.xml')  

# Starting Capture
cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Turning capture into gray pixels
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Using Face Detection Cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    
    # Using Face Detection Cascade
    faces2 = face_cascade2.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    
    # # Using Face Detection Cascade
    # faces3 = face_cascade3.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # - Loop Sections -

    # FACE
    for (x,y,w,h) in faces:
        # Numbers of x_start - y_start - x_end - y_end
        print(x, y, w, h)  
        
        # (ycord_start, ycord_end) & same thing for x
        roi_gray = gray[y:y+h, x:x+w]
        
        # for a colored capture
        roi_color = frame[y:y+h, x:x+w]
        
        # Saving the last face and this is file name for picture
        img_item = "my_image.png" 
        
        # Saving last image photo (Gray)
        cv.imwrite(img_item, roi_gray)
        
        # Rectangle BGR, thickness, width and height
        color = (0, 0, 255)
        border = 2
        width = x + w
        height = y + h

        # Drawing rectangle
        if faces.all() == True:
            cv.rectangle(frame, (x, y), (width, height),color, border)
            # cv.rectangle(CAPTURE, (X_Start, Y_Start), (X_End, Y_End), Rectangle BGR, Rectangle Border)

    # PROFILE FACE
    for (q, z, v, j) in faces2:
        # All the same as face

        print(q, z, v, j)

        roi_gray = gray[z:z + j, q:q + v]
        roi_color = frame[z:z + j, q:q + v]

        img_item = "my_image2.png"
        cv.imwrite(img_item, roi_gray)

        color = (0, 0, 255) 
        border = 2
        width2 = q + v
        height2 = z + j

        if faces2.all() == True:
            cv.rectangle(frame, (q, z), (width2, height2), color, border)
            # cv.rectangle(CAPTURE, (X_Start, Y_Start), (X_End, Y_End), Rectangle BGR, Rectangle Border)

    # CAT
    # for (q, z, v, j) in faces3:
        # All the same as face

        # print(q, z, v, j)

        # roi_gray = gray[z:z + j, q:q + v]
        # roi_color = frame[z:z + j, q:q + v]

        # img_item = "my_image2.png"
        # cv.imwrite(img_item, roi_gray)
        
        # color = (0, 0, 255)
        # border = 2
        # width2 = q + v
        # height2 = z + j
        
        # if faces3.all() == True:
            # cv.rectangle(frame, (q, z), (width2, height2), color, border)
            # cv.rectangle(CAPTURE, (X_Start, Y_Start), (X_End, Y_End), Rectangle BGR, Rectangle Border)


    # Displaying the resulting frame
    cv.imshow('frame', frame)

    # # Gray display (If you wanna show)
    # cv.imshow('gray', gray)

    if cv.waitKey(20) and 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
