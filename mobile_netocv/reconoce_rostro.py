import cv2

# Cargar el clasificador en cascada para la deteccin de rostros
clasificador = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')

# Leer la imagen
imagen = cv2.imread('./images/foto2.jpg')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar rostros en la imagen
rostros = clasificador.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)

# Dibujar rectngulos alrededor de los rostros detectados
for (x, y, w, h) in rostros:
    cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Mostrar la imagen con los rostros detectados
cv2.imshow('Rostros Detectados', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()