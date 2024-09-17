import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)
cv.namedWindow("Cam")

esc = False
while not esc:
    if cv.waitKey(10) & 0xFF == 27 or cv.getWindowProperty("Cam", cv.WND_PROP_VISIBLE) < 1.0: esc = True 

    # Recogo el frame y lo muestro 
    _, frame = cam.read()
    cv.imshow("Cam", frame)

    img1 = frame
    img_cnt = cv.cvtColor(img1, cv.COLOR_RGB2RGBA)
    # img_cnt = cv.cvtColor(img1, cv.COLOR_BGR2RGB)

    # Lo paso a hsv y recogo solamente el valor V
    img1 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
    img1 = img1[:,:,2] # img1 = img1[:,:,-1]

    # cv.GaussianBlur(img1, (5,5), 10, 10) # ??????
    ret, th1 = cv.threshold(img1, 140, 255, cv.THRESH_BINARY)
    kernel = np.ones((5,5), np.uint8)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))

    img2 = cv.morphologyEx(th1, cv.MORPH_OPEN, kernel, iterations=8)
    img2 = cv.morphologyEx(img2, cv.MORPH_CLOSE, kernel, iterations=2)

    umbral_minimo = 50
    umbral_maximo = 100

    cn = cv.Canny(img2, umbral_minimo, umbral_maximo)
    contornos, _ = cv.findContours(cn.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contornos:
        M = cv.moments(cnt)

        if M['m00'] != 0:
            cx = int(M["m10"]/M['m00'])
            cy = int(M["m01"]/M['m00'])
            cv.circle(img_cnt, (cx,cy), 5, (0,0,255),4)

        area = cv.contourArea(cnt)
        perimetro = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, 0.001*perimetro, True)
        cv.drawContours(img_cnt, [approx], -1, (0,255,0),4)
        # TODO dado el perimetro y el area decir si es piedra,papel o tijera

        cv.imshow("Contornos", img_cnt)

cam.release() 
cv.destroyAllWindows()