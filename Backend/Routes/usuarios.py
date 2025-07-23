#coleccion de los usuarios importamos las rutas
#api ruter define las rutas por aparte dentro del archivo 
from fastapi import APIRouter,Responses,status
from Backend.config.mongo import usuarios_collection
from Backend.Schemas.user import userEntity, usersEntity
from Backend.Models.user import usuarios as Usuarios
from Backend.utils.seguridad import hash_to_brainfuck
from bson import ObjectId #invierte un string a un objeto de tipo ObjectId
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

#coleccion de usuarios donde APIRouter llamar a esta cadena por post
usuarios=APIRouter()





@usuarios.get('/usuarios')#obtener usuarios
def buscar_usuarios():
    return usersEntity(usuarios_collection.find())

#funcion que devuelve una lista de usuarios
#def obtener_usuarios():
 #   return {"usuarios": ["usuario1", "usuario2", "usuario3"]}

@usuarios.post('/usuarios')#crear usuario
def crear_usuarios(usuario: Usuarios):
    new_usuario = usuario.dict()
    new_usuario["pass_hash"] = hash_to_brainfuck(usuario.pass_hash)
    id = usuarios_collection.insert_one(new_usuario).inserted_id
    usuario= usuarios_collection.find_one({"_id": id})
    return str(id)

@usuarios.get('/usuarios/{id}')#obtener usuario por id
def buscar_unico_usuario(id: str):
    return userEntity(usuarios_collection.find_one({"_id": ObjectId(id)}))



@usuarios.put('/usuarios/{id}')#obtener usuario por id
def actualizar_usuario(id: str, usuario: Usuarios):
    usuarios_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": usuario.dict(exclude_unset=True, exclude={"pass_hash"})}
        )
    return {"mensaje": f"Hola Mundo desde la ruta de usuarios con id {id}"}  


@usuarios.delete('/usuarios/{id}')#obtener usuario por id
def borrar_usuario(id: str):
  userEntity(usuarios_collection.find_one_and_delete({"_id": ObjectId(id)}))
  return Responses(status_code=status.HTTP_204_NO_CONTENT) #no content

