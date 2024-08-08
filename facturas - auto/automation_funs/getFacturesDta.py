import pyautogui as auto
import pytesseract as tess
import re
import time
# Configura la ruta al ejecutable de Tesseract
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def get_User():
    auto.hotkey('win', 'up') #maximiza la app
    # Especificar la región para la captura de pantalla (left, top, width, height)
    region = (1, 41, 500, 38)
    time.sleep(2)
    # Tomar captura de pantalla de la región especificada
    screenshot = auto.screenshot(region=region)
    
    # Usar pytesseract para extraer texto de la captura de pantalla
    email_user = tess.image_to_string(screenshot)
    
    # Limpiar el texto extraído para eliminar caracteres no deseados
    email_user = email_user.strip()
    
    # Verificar si el texto contiene un correo electrónico válido usando una expresión regular
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    match = re.search(email_pattern, email_user)
    
    if match:
        return match.group(0)
    else:
        return "No se encontro usaurio"

def get_products(): #Productos de la factura
    auto.hotkey('win', 'up') #maximiza la app
    time.sleep(2)
    #Region a capturar
    region = (3, 109, 540,90)
    # Tomar captura de pantalla de la región especificada
    screenshot = auto.screenshot(region=region)
    # Usar pytesseract para extraer texto de la captura de pantalla
    products_text = tess.image_to_string(screenshot)
    return {"Productos": products_text}

def get_total(): #Total a pagar
    auto.hotkey('win', 'up') #maximiza la app
    time.sleep(2)
    # Region a capturar
    region = (4, 195, 170, 105)
    # Tomar captura de pantalla de la región especificada
    screenshot = auto.screenshot(region=region)
    # Usar pytesseract para extraer texto de la captura de pantalla
    total_text = tess.image_to_string(screenshot)
    total_pattern = r"Total a pagar\s*:\s*(\d+)"
    match = re.search(total_pattern, total_text)
    if match:
        total_text = match.group(1)
        return {"total": int(match.group(1))}
    else:
        return {"Error": "No se encontro el total a pagar"}
def get_status():
    auto.hotkey('win', 'up') #maximiza la app
    time.sleep(2)
    # Region a capturar
    region = (4, 286, 200, 300)
    # Tomar captura de pantalla de la región especificada
    screenshot = auto.screenshot(region=region)
    # Usar pytesseract para extraer texto de la captura de pantalla
    status_text = tess.image_to_string(screenshot)
    if "Pago" in status_text: #Estado pago de la factura
        return "Pago"
    elif "Sin pagar" in status_text:
        return  "Sin pagar"
    else:
        return "Error: No se encontro el estado de la factura"
    
print(get_status())