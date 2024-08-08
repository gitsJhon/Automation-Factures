import pyautogui
import time

#Usa este archivo para verificar las coordenadas del mouse :)

print("Mueve el mouse a la esquina superior izquierda de la región.")
time.sleep(5)  # Te da 5 segundos para mover el mouse a la posición deseada
x1, y1 = pyautogui.position()
print(f"Esquina superior izquierda: ({x1}, {y1})")

print("Mueve el mouse a la esquina inferior derecha de la región.")
time.sleep(5)  # Te da 5 segundos para mover el mouse a la posición deseada
x2, y2 = pyautogui.position()
print(f"Esquina inferior derecha: ({x2}, {y2})")

# Calcula el ancho y el alto de la región
width = x2 - x1
height = y2 - y1

print(f"Dimensiones de la región: Ancho={width}, Alto={height}")
