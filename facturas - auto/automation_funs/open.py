import pyautogui as auto #Libreria de auomatizacion
import time #para los tiempos de carga

id = 3 #ejemplo de ID
def open_folder(click = 2): #funcion encargada de abrir la carpeta co las facturas
    try:
        auto.moveTo(45,270) #position de la carpeta
        time.sleep(2)
        auto.click(clicks=2)
    except auto.FailSafeException: #Error de seguridad interno de la libreria Pyautigui
        return {"Mensaje": "Error de seguridad de Pyautogui"}
    except Exception as e: #No se pudo abrir la carpeta
        return {"Mensaje": f"Error desconocido: {str(e)}, Fallo al abrir la carpeta"}

def open_facture(id, clicks =2): #abre el folder segund la ID, decidi que es mas practico no pasar las coordenadas como parametros
    if id == 1:
        auto.moveTo(510, 269) #posicion de la factura 1
        time.sleep(2)
        auto.click(clicks=clicks)
    elif id == 2:
        auto.moveTo(514, 290) #posicion de la factura 2
        time.sleep(2)
        auto.click(clicks=clicks)
    elif id == 3:
        auto.moveTo(525, 315) #posicion de la factura 3
        time.sleep(2)
        auto.click(clicks=clicks)
    else:
        return {"Mensaje": "ID de factura no válido"} #por si se ingresa una ID no valida

