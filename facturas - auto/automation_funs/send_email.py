import pyautogui as auto
import time
def send(email_user:str, clicks = 1):
    oultlook_position = (403,747) #Defino como variable para personalizacion de escritorio
    auto.moveTo(oultlook_position)
    time.sleep(2)
    auto.click(clicks=1)
    time.sleep(15) #La app a veces demora mucho en abrir
    auto.hotkey('win', 'up') #Maximia la app
    auto.moveTo(122,108) #Boton de enviar nuevo correo
    time.sleep(2)
    auto.click(clicks=clicks)
    time.sleep(1)
    auto.moveTo(777,209) #Campo del correo
    time.sleep(1)
    auto.write(email_user)
    time.sleep(1)
    auto.moveTo(656,261) #Campo del asunto
    time.sleep(1)
    auto.click(clicks=clicks)
    time.sleep(1)
    auto.write("Recordatorio de pago")
    time.sleep(1)
    auto.moveTo(808,356) #Cuerpo del email
    time.sleep(1)
    auto.click(clicks=clicks)
    auto.write("Hola,\nTe recordamos que tu factura se encuentra por pagar.\nPor favor paga antes de la fecha limite.\n\nSaludos")
    time.sleep(1)
    auto.moveTo(677,156)
    time.sleep(1)
    auto.click(clicks=clicks) #Enviar el email
    return {"status": "Email enviado"}