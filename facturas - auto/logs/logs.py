import datetime

def log_get_user(user:str):
    text = "logs.txt"
    hora = datetime.datetime.now()
    fecha_hora_formateada = hora.strftime("%d-%m-%Y %H:%M:%S")
    with open(text, 'a') as archive:
        archive.write(f"Se obtuvo el usuario : {user} - {fecha_hora_formateada}" + '\n')
def log_get_total(id:int):
    text = "logs.txt"
    hora = datetime.datetime.now()
    fecha_hora_formateada = hora.strftime("%d-%m-%Y %H:%M:%S")
    with open(text, 'a') as archive:
        archive.write(f"Se obtuvo el total a pagar de la factura con id: {id} - {fecha_hora_formateada}" + '\n')
def log_get_pago(id:int):
    text = "logs.txt"
    hora = datetime.datetime.now()
    fecha_hora_formateada = hora.strftime("%d-%m-%Y %H:%M:%S")
    with open(text, 'a') as archive:
        archive.write(f"Se consulto el estado de pago de la factura con id: {id} - {fecha_hora_formateada}" + '\n')
def log_get_products(id:int):
    text = "logs.txt"
    hora = datetime.datetime.now()
    fecha_hora_formateada = hora.strftime("%d-%m-%Y %H:%M:%S")
    with open(text, 'a') as archive:
        archive.write(f"Se obtuvieron los productos de la factura con id: {id} - {fecha_hora_formateada}" + '\n')
