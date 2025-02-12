import cv2

# Leer una imagen
imagen = cv2.imread('ruta/a/tu/imagen.jpg')

# Mostrar la imagen en una ventana
cv2.imshow('Imagen', imagen)

# Esperar hasta que se presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas
cv2.destroyAllWindows()