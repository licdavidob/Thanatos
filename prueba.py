import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import datetime

capture = cv2.VideoCapture(0)

# Crear el objeto QRCodeDetector
qrDecoder = cv2.QRCodeDetector()

# Configurar los parámetros para la detección de bordes
low_threshold = 100
high_threshold = 200
aperture_size = 3

while True:
    ret, frame = capture.read()

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Reducir el ruido en la imagen
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Detectar los bordes en la imagen
    edges = cv2.Canny(blurred, low_threshold, high_threshold, aperture_size)

    # Buscar los contornos en la imagen
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en la imagen original
    cv2.drawContours(frame, contours, -1, (0, 0, 255), 2)

    # Decodificar códigos QR
    decoded_objs = pyzbar.decode(frame)

    # Imprimir los datos de los códigos QR y guardar una imagen del cuadro actual
    for obj in decoded_objs:
        data = obj.data.decode()
        print(f'Dato: {data}')

        # Guardar una imagen del cuadro actual con un nombre único basado en la fecha y hora actual
        

    # Mostrar el cuadro de video en la ventana
    cv2.imshow('Webcam', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Cerrar la ventana de la webcam y liberar la cámara
cv2.destroyAllWindows()
capture.release()
