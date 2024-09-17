import cv2 as cv
import numpy as np

DATA_DIR = "IA/Programacion/Learning/opencv/archives/"
color_punto = None

def click_raton(event, x, y, flags, param):
    global color_punto
    if event == cv.EVENT_LBUTTONDBLCLK:
        b, g, r = img1[y, x]
        # Lo metemos en un array de esta forma para hacer "una imagen de un solo punto"
        # de esta manera podremos pasarla a otros tipos de colores ("hsv, rgb")
        color_punto = np.uint8([[[b, g, r]]]) 
        color_punto = cv.cvtColor(color_punto, cv.COLOR_BGR2HSV)
        print(f"Click en {x}, {y}, color = {color_punto}")

src1 = cv.imread(DATA_DIR + "nemo.jpg")
cv.namedWindow("Imagen")
cv.setMouseCallback("Imagen", click_raton)

img1 = src1
hsv = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
cv.imshow("Imagen", img1)

esc = False
while not esc:
    if color_punto is not None:
        color_ini = np.array([color_punto[0,0,0] - 10,10,10])
        color_end = np.array([color_punto[0,0,0] + 10,255,255])
        mascara = cv.inRange(hsv, color_ini, color_end)

        # color_minimo = (color_punto[0,0,0] - [10,10,10])
        # color_maximo = (color_punto[0,0,0] + [10,255,255])
        # mascara = cv.inRange(hsv, color_minimo, color_maximo)
        cv.namedWindow("Mascara")
        cv.imshow("Mascara", mascara)
        color_punto = None
    if cv.waitKey(10) & 0xFF == 27 or cv.getWindowProperty("Imagen", cv.WND_PROP_VISIBLE) < 1.0: esc = True