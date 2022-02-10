import os
from PIL import Image
import numpy as np
import cv2 as cv
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

current_id = 0
label_ids = {}
y_labels = list()
x_train = list()


for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ","-").lower()
            print(label, path)
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            print(label_ids)
            # y_labels.append(label)
            # x_train.append(path)
            pil_image = Image.open(path).convert("L") # grayscale
            image_array = np.array(pil_image, "uint8")
            print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

# print(y_labels)
# print(x_train)

with open("labels.picle", 'wb') as f:
    pickle.dump(label_ids, f)


