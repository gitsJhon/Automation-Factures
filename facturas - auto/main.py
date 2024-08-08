from fastapi import FastAPI
from dotenv import load_dotenv
from outh import auth_routes
from automation_funs.getFacturesDta import get_products, get_status, get_total, get_User
from automation_funs.open import open_folder, open_facture
from facture import facture_route

app = FastAPI()
app.include_router(auth_routes, prefix="/login") #ruta de login y verificacion de login
app.include_router(facture_route, prefix="/factures") #ruta para obtener el estado de las facturas