#coleccion de los usuarios importamos las rutas
#api ruter define las rutas por aparte dentro del archivo 
from fastapi import APIRouter,Response, status
from Backend.config.mongo import usuarios_collection
from Backend.Schemas.user import userEntity, usersEntity
from Backend.Models.user import usuarios as Usuarios
from Backend.utils.seguridad import hash_to_brainfuck
from bson import ObjectId #invierte un string a un objeto de tipo ObjectId

#coleccion de usuarios donde APIRouter llamar a esta cadena por post
usuarios=APIRouter()

#tagas nos permite agrupar las rutas en la documentacion de la api agrupa las rutas de usuarios
@usuarios.get('/usuarios',response_model=list[Usuarios],tags=["usuarios"])#obtener usuarios y su lista del objeto
def buscar_usuarios():
    return usersEntity(usuarios_collection.find())
#funcion que devuelve una lista de usuarios
#def obtener_usuarios():
 #   return {"usuarios": ["usuario1", "usuario2", "usuario3"]}

@usuarios.post('/usuarios', response_model=Usuarios,tags=["usuarios"])#crear usuario con una lista de usuarios
def crear_usuarios(usuario: Usuarios):
    new_usuario = usuario.dict()
    new_usuario["pass_hash"] = hash_to_brainfuck(usuario.pass_hash)
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