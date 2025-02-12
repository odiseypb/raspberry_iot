import cv2 
import numpy as np
import time
from gpiozero import LED

# Configurar LED para alerta
led = LED(17)  # GPIO donde es conectado el LED

# Cargar modelo preentrenado (MobileNet SSD)
#modelo descargado de: https://github.com/MediosZ/MobileNet-SSD/blob/master/mobilenet/MobileNetSSD_deploy.prototxt
prototxt = "./data/MobileNetSSD_deploy.prototxt"
caffemodel = "./data/MobileNetSSD_deploy.caffemodel"
net = cv2.dnn.readNetFromCaffe(prototxt, caffemodel)

# Lista de clases reconocidas
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair",
           "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

# Captura de video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir imagen en blob para la red neuronal
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # Procesar detecciones
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Umbral de confianza
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Dibujar la caja y etiqueta
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            text = f"{label}: {confidence:.2f}"
            cv2.putText(frame, text, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Si detecta una botella, activa el LED
            if label == "bottle":
                led.on()
                print("¡Botella detectada! LED activado")
                time.sleep(1)
                led.off()

    cv2.imshow("Reconocimiento de Objetos", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

