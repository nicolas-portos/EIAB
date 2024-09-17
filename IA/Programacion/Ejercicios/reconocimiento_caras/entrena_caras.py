import cv2 as cv
import matplotlib.pyplot as plt
import pylab # this allows you to control figure size
import numpy as np
import os, pickle

pylab.rcParams['figure.figsize'] = (15.0, 10.0)
PATH = "IA/Programacion/Ejercicios/reconocimiento_caras/"
MODEL = cv.face.LBPHFaceRecognizer_create()

dfaces = {"ayuso":0,"bukele":1,"rajoy":2,"trevijano":3}
lcaras = []
values = []

for person in os.listdir(PATH+"images/"):
    for image in os.listdir(PATH+"images/"+person):
        src = cv.imread(f"{PATH}images/{person}/{image}")
        img = cv.cvtColor(src, cv.COLOR_BGR2RGB)
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
        face = face_cascade.detectMultiScale(image = gray, scaleFactor = 1.25, minNeighbors = 6, minSize = (30,30))

        for (x,y,w,h) in face:
            cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            values.append(dfaces[person])
            lcaras.append(roi_gray)
            # ojos = eye_cascade.detectMultiScale(roi_gray, 3, 1)
            ojos = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in ojos:
                cv.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255, 0), 2)

        plt.imshow(img)
        plt.show()

MODEL.train(lcaras, np.array(values))
MODEL.save("IA/Programacion/Ejercicios/reconocimiento_caras/archives/trained_model.xml")

with open(f'{PATH}archives/values.pickle', 'wb') as f:
    pickle.dump(dfaces, f)