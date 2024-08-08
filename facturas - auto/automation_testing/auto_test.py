import pyautogui as auto
import time
import pytesseract as tess

#Este archivo sirve para hacer testing sobre los valores que regresa las funciones de las facturas
#Recuertda que debes tener abierta la factura objetivo de el testeo
#Se espera que se retorne los valores que captura pytesseract
def get_user():
    auto.hotkey('win', 'up') #maximiza la app
    # Especificar la región para la captura de pantalla (left, top, width, height)
    region = (1, 41, 500, 38)
    time.sleep(2)
    # Tomar captura de pantalla de la región especificada
    screenshot = auto.screenshot(region=region)
    # Usar pytesseract para extraer texto de la captura de pantalla
    email_user = tess.image_to_string(screenshot)
    return email_user

def get_products():
    auto.hotkey('win', 'up') #maximiza la app
    time.sleep(2)
    #Region a capturar
    region = (3, 109, 540,90)
    # Tomar captura de pantalla de la región especificada
    screenshot = auto.screenshot(region=region)
    # Usar pytesseract para extraer texto de la captura de pantalla
    products_text = tess.image_to_string(screenshot)
    return products_text

def get_total():
    auto.hotkey('win', 'up') #maximiza la app
    time.sleep(2)
    # Region a capturar
    region = (4, 195, 170, 105)
    # Tomar captura de pantalla de la región especificada
    screenshot = auto.screenshot(region=region)
    # Usar pytesseract para extraer texto de la captura de pantalla
    total_text = tess.image_to_string(screenshot)
    return total_text

def get_status():
    auto.hotkey('win', 'up') #maximiza la app
    time.sleep(2)
    # Region a capturar
    region = (4, 286, 200, 300)
    # Tomar captura de pantalla de la región especificada
    screenshot = auto.screenshot(region=region)
    # Usar pytesseract para extraer texto de la captura de pantalla
    status_text = tess.image_to_string(screenshot)
    return status_text

# Ahora que tenemos las funciones para capturar los valores, podemos probarlas con la factura objetivo

print(get_status) # cambia segun la funcion que sedeas probar, el valor capturado se imprimira en la terminal