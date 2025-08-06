#coleccion de los usuarios importamos las rutas
#api ruter define las rutas por aparte dentro del archivo 
from datetime import datetime
from fastapi import APIRouter, HTTPException, Request,Response, status
from pydantic import BaseModel
from Backend.config.mongo import usuarios_collection
from Backend.Schemas.user import userEntity, usersEntity
from Backend.Models.user import usuarios as Usuarios
from Backend.utils.seguridad import hash_to_brainfuck
from bson import ObjectId #invierte un string a un objeto de tipo ObjectId

#coleccion de usuarios donde APIRouter llamar a esta cadena por post
usuarios=APIRouter()

#tags nos permite agrupar las rutas en la documentacion de la api agrupa las rutas de usuarios
@usuarios.get('/usuarios',response_model=list[Usuarios],tags=["usuarios"])#obtener usuarios y su lista del objeto
def buscar_usuarios():
    return usersEntity(usuarios_collection.find())
#funcion que devuelve una lista de usuarios
#def obtener_usuarios():
 #   return {"usuarios": ["usuario1", "usuario2", "usuario3"]}

@usuarios.post('/usuarios', response_model=Usuarios,tags=["usuarios"])#crear usuario con una lista de usuarios
def crear_usuarios(usuario: Usuarios):
    new_usuario = usuario.dict()
    new_usuario["pass_hash"] = hash_to_brainfuck(usuario.pass_hash, usuario.email)
    id = usuarios_collection.insert_one(new_usuario).inserted_id
    usuario= usuarios_collection.find_one({"_id": id})
    return str(id)



@usuarios.get('/usuarios/{id}', response_model=Usuarios,tags=["usuarios"])#obtener usuario por id
def buscar_unico_usuario(id: str):
    return userEntity(usuarios_collection.find_one({"_id": ObjectId(id)}))



@usuarios.put('/usuarios/{id}', response_model=Usuarios,tags=["usuarios"])#obtener usuario por id
def actualizar_usuario(id:str ,user: Usuarios):
    #busqueda de la db
    usuarios_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": user.dict()})# actualiza el usuario por id
    return userEntity(usuarios_collection.find_one({"_id": ObjectId(id)})) ##actualiza el usuario por id



@usuarios.delete('/usuarios/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["usuarios"])#obtener usuario por id
def borrar_usuario(id: str):
    userEntity(usuarios_collection.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=status.HTTP_204_NO_CONTENT)  # No content response after deletion

#clase para nuestro login de vue 
class LoginInput(BaseModel):
    email: str
    password: str  

#si el suuario esta en login usamos el tag de auth para la coleccion de datos 
@usuarios.post('/login', tags=["auth"])
def login_user(datos: LoginInput):
    print(" Datos recibidos:", datos.dict())  # debug para ver si funciona 
    # Aplicar el hash personalizado para seguridad
    hashed_password = hash_to_brainfuck(datos.password, datos.email)
    # Buscar el usuario con email y hash
    usuario = usuarios_collection.find_one({"email": datos.email,"pass_hash": hashed_password})
    # Validación si el usuario es por un token mas el usuario del emial es para seguridad
    if usuario:
        return {"token": "fake-jwt-for-" + usuario["email"]}
    # Si no coincide
    raise HTTPException(status_code=401, detail="Credenciales inválidas")

@usuarios.put("/register",tags=["auth"])
async def register_users(request:Request):
    datos=await request.json()
    print("Datos recibidos de froma correcta ",datos)
    #validamos que tengamos datos minimos del front
    if not all(i in datos for i in ("usuario","email","password")):
        raise HTTPException(status_code=422,detail="Faltan campos obligatorios")
    #verificamos duplicados
    if usuarios_collection.find_one({"email":datos["email"]}):
        raise HTTPException(status_code=400,detail="El correo ya esta registrado")
    hashed_password=hash_to_brainfuck(datos["password"],datos["email"])
    #crear el usuario con los datos minimos y por defecto 
    nuevo_usuario={
        "usuario": datos["usuario"],
        "email": datos["email"],
        "pass_hash": hashed_password,
        "rol": "gratis",
        "pago": False,
        "activo": True,
        "logueo": {
            "fecha": datetime.utcnow(),
            "conteo": 0
        },
        "plan": {
            "nombre": "gratuito",
            "fecha_inicio": datetime.utcnow(),
            "fecha_fin": None
    }
    }
 # Insertar
    result = usuarios_collection.insert_one(nuevo_usuario)
    return {
        "mensaje": "Usuario registrado correctamente",
        "token": "fake-jwt-for-" + datos["email"],
        "user_id": str(result.inserted_id)
    }