import cv2 as cv
import numpy as np

color_punto = None

def click_raton(event, x, y, flags, param):
    global color_punto
    # Si el evento es un click izquierdo 
    if event == cv.EVENT_FLAG_LBUTTON:
        # Recoger los valores bgr del frame en el punto que hemos hecho click
        b, g, r = frame[y, x]
        # Lo metemos en un array de esta forma para hacer "una imagen de un solo punto"
        # de esta manera podremos pasarla a otros tipos de colores ("hsv, rgb") si queremos
        color_punto = np.uint8([[[b, g, r]]]) 
        color_punto = cv.cvtColor(color_punto, cv.COLOR_BGR2HSV)

def crear_mascara(frame):
    # Le sumamos y restamos valores al color punto para poder recoger con mayor precisión la diferencia de un color
    # Al hacer esto cogemos el color rojo (click_raton) y creamos con estos valores un rango de rojos para que 
    # al pasarlos a hsv estos aparezcan de color blanco y el resto en negro
    # Convertimos el frame a colores hsv que deje el video con dos valores [negro, blanco]
    color_ini = np.array([color_punto[0,0,0] - 10,10,10])
    color_end = np.array([color_punto[0,0,0] + 10,255,255])
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mascara = cv.inRange(hsv, color_ini, color_end)
    cv.imshow("Mascara", mascara)
    return mascara

cam = cv.VideoCapture(0) # Creamos la captura de la camara
cv.namedWindow("DroidCam") # Le damos un nombre a la ventana donde se mostrara

esc = False
imagen_fondo = None

while not esc:
    # press esc or close window to stop
    if cv.waitKey(10) & 0xFF == 27 or cv.getWindowProperty("DroidCam", cv.WND_PROP_VISIBLE) < 1.0: esc = True 
    
    # Recogemos los frames de la camara y los mostramos por la ventana
    _, frame = cam.read() # frame = cam.read()[1]
    cv.imshow("DroidCam", frame)
    cv.setMouseCallback("DroidCam", click_raton)

    if cv.waitKey(10) & 0xFF == 32: imagen_fondo = frame # Creamos el fondo

    if color_punto is not None: mascara = crear_mascara(frame) # Creamos la mascara y el color_punto

    if imagen_fondo is not None:
        # Chroma hecho con colores
        # fondo_negro = cv.inRange(mascara, 0,128) # Cogemos los valores negros de la mascara
        # fondo_blanco = cv.inRange(mascara, 129,255) # Cogemos los valores blancos de la mascara

        # img1 = cv.bitwise_and(frame, frame, mask = fondo_negro) # Cuando el video de la mascara sea negro dejar la mascara
        # img2 = cv.bitwise_and(imagen_fondo, imagen_fondo, mask = fondo_blanco) # Cuando el video de la mascara sea blanca cambiar por la imagen de fondo
        
        # cv.imshow("Chroma", cv.add(img1,img2)) # Juntamos las dos imagenes para mostrarlas

        # Chroma hecho con operaciones lógicas
        # La mascara es color que hemos elegido con color_punto
        # Mostrar la imagen de fondo en donde se encuentre la mascara
        # Mostrar el frame actual donde no este la mascara
        cv.imshow("Chroma_logico", 
                  cv.bitwise_or(
                        cv.bitwise_and(imagen_fondo, imagen_fondo, mask=mascara),
                        cv.bitwise_and(frame, frame, mask= cv.bitwise_not(mascara))
                    ))

cam.release() 
cv.destroyAllWindows()