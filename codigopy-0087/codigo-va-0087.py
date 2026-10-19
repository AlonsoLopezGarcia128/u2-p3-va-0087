# Alonso Lopez Garcia NC = 0087
# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
# ruta de la imagen
ruta_imagen = os.path.join(
    "img-original-0087",
    "img-gorila-0087.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
gorila = cv2.imread(ruta_imagen)
print(gorila)
# print(gorila) muestra las matrices de la imagen 
# Convertir BGR a RGB color rojo COLOR_BGR2RGB 
gorilita = cv2.cvtColor(gorila, cv2.COLOR_BGR2RGB) 
cv2.imshow("gorila 0087", gorilita)
cv2.waitKey(0) # Tiempo de espera
cv2.destroyAllWindows() # Destruye todas las ventanas en memoria 

print("Alonso López García NC = 0087")