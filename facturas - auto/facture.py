from fastapi import FastAPI, APIRouter, Query
from dotenv import load_dotenv
from outh import auth_routes
from automation_funs.getFacturesDta import get_products, get_status, get_total, get_User
from automation_funs.open import open_folder, open_facture
from automation_funs.close_apps import close_window
from automation_funs.send_email import send
from logs.logs import log_get_pago, log_get_products, log_get_total, log_get_user
import time
facture_route = APIRouter()

@facture_route.get("/status") #Factura
def facture_status(id: int = Query(...), password: str = Query(...)):
    if password == "your_password":
        open_folder()
        time.sleep(1)
        open_facture(id)
        time.sleep(1)
        get_status()
        if get_status() == "Pago":
            close_window()
            log_get_pago(id)
            return "Pago"
        elif get_status() == "Sin Pagar":
            close_window
            log_get_pago(id)
            user = get_User()
            if user == "No se encontro el usuario":
                close_window
                return "Pemdiente, Error al encontrar el usuario"
            else:
                close_window()
                send(user)
                close_window()
                log_get_pago(id)
                return "Pendiente, se envio el correo"
        else:
            close_window()
            return "Error en el estado de la factura"
    else:
        return  "Contraseña incorrecta"

@facture_route.get("/total")
def facture_total(id: int = Query(...), password: str = Query(...)):
    if password == "your_password":
        open_folder()
        time.sleep(1)
        open_facture(id)
        time.sleep(1)
        total = get_total()
        time.sleep(4)
        close_window()
        log_get_total(id)
        return total
    else:
        return "Contraseña incorrecta"
    
@facture_route.get("/user")
def facture_user(id: int = Query(...), password: str = Query(...)):
    if password == "your_password":
        open_folder()
        time.sleep(1)
        open_facture(id)
        time.sleep(4)
        user = get_User()
        time.sleep(4)
        close_window()
        log_get_user(user)
        return user

    else:
        return "Contraseña incorrecta"
@facture_route.get("/products")
def facture_products(id: int = Query(...), password: str = Query(...)):
    if password == "your_password":
        open_folder()
        time.sleep(1)
        open_facture(id)
        time.sleep(1)
        products = get_products()
        if products == "":
            close_window()
            return "No se pudieron obtener los productos"
        else:
            close_window()
            log_get_products(id)
            return products
    else:
        return "Contraseña incorrecta"
@facture_route.get("/info")
def facture_info(id: int = Query(...), password: str = Query(...)):
    if password == "your_password":
        open_folder()
        time.sleep(1)
        open_facture(id)
        time.sleep(1)
        status = get_status()
        total = get_total()["total"]
        user = get_User()
        products = get_products()["Productos"]
        if status == "":
            close_window()
            return "No se pudo obtener el estado de la factura"
        elif total == 0:
            close_window()
            return "No se pudo obtener el total de la factura"
        elif user == "":
            close_window()
            return "No se pudo obtener el usuario de la factura"
        elif products == "":
            close_window()
            return "No se pudieron obtener los productos"
        else:
            if status == "Pago":
                time.sleep(15)
                close_window()
                log_get_products(id)
                log_get_pago(id)
                log_get_total(id)
                log_get_user(user)
                return {"Status": status, "Total": total, "User": user, "Products": products}
            elif status == "Sin Sin Pagar":
                close_window()
                send(user)
                close_window()
                return {"Status": status, "Total": total, "User": user, "Products": products, "Recordatorio enviado": True}
    else:
        return "Contraseña incorrecta"
load_dotenv()
app = FastAPI()
app.include_router(auth_routes, prefix="/login") #ruta de login y verificacion de login
app.include_router(facture_route, prefix="/factures") #ruta para obtener el estado de las facturas
