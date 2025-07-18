#coleccion de los usuarios importamos las rutas
#api ruter define las rutas por aparte dentro del archivo 
from fastapi import APIRouter
from Backend.config.mongo import usuarios_collection
from Backend.Schemas.user import userEntity, usersEntity

#coleccion de usuarios donde APIRouter llamar a esta cadena por post
usuarios=APIRouter()
@usuarios.get('/usuarios')#obtener usuarios
def buscar_usuarios():
    return usersEntity(usuarios_collection.find())

#funcion que devuelve una lista de usuarios
#def obtener_usuarios():
 #   return {"usuarios": ["usuario1", "usuario2", "usuario3"]}

@usuarios.post('/usuarios')#crear usuario
def crear_usuarios():
    return {"mensaje": "Hola Mundo desde la ruta de usuarios"}  

@usuarios.get('/usuarios/{id}')#obtener usuario por id
def buscar_unico_usuario(id: str):
    return {"mensaje": f"Hola Mundo desde la ruta de usuarios con id {id}"}  



@usuarios.put('/usuarios/{id}')#obtener usuario por id
def actualizar_usuario():
    return {"mensaje": f"Hola Mundo desde la ruta de usuarios con id {id}"}  


@usuarios.delete('/usuarios/{id}')#obtener usuario por id
def borrar_usuario():
    return {"mensaje": f"Hola Mundo desde la ruta de usuarios con id {id}"}  


