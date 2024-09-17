import cv2 as cv
import matplotlib.pyplot as plt
import pylab # this allows you to control figure size
import os, pickle

pylab.rcParams['figure.figsize'] = (15.0, 10.0)
PATH = "IA/Programacion/Ejercicios/reconocimiento_caras/"
model = cv.face.LBPHFaceRecognizer.create()
model.read(filename=f"{PATH}archives/trained_model.xml")

with open(f'{PATH}archives/values.pickle', 'rb') as f:
    values = pickle.load(f)

lnames = {value: key for key, value in values.items()}

for image in os.listdir(PATH+"test/"):
    src = cv.imread(f"{PATH}test/{image}")
    img = cv.cvtColor(src, cv.COLOR_BGR2RGB)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))

    for (x,y,w,h) in face:
        names, confidence = model.predict(gray[y:y + h, x:x + w])
        print(confidence)
        cv.putText(img, lnames[names], (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)   

    plt.imshow(img)
    plt.show()     