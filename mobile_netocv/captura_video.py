import cv2

# Iniciar la
captura = cv2.VideoCapture(0)

while True:
    # Capturar frame por frame
    ret, frame = captura.read()

    # Mostrar el frame en una ventana
    cv2.imshow('Video en Vivo', frame)

    # Salir si se presiona la tecla q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar las ventanas
captura.release()
cv2.destroyAllWindows()