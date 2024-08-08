from fastapi import APIRouter, Header
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse
auth_routes = APIRouter()

class User(BaseModel):  #Modelo base de los datos de login, para este ejemplo se usara solamente username
    username: str
    email: EmailStr
@auth_routes.post("/login") #Ruta de login
def login(user: User):
    print(user)
    if user.username == "David": #Nombre de prueba para login
        password = "your_password" #de ejemplo
        return password #retorna contraseña
    else:
        return JSONResponse(content= {"Mensagge": "User not found"}, status_code=404)