#esquema de que va a tener la base de datos
#coleccion de usuarios importamos las rutas
#definimos una funcion el cual sera objeto que nos regresa un diccionario 
def userEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "Usuario": item.get("Usuario"),
        "PassHash": item.get("PassHash"),
        "Correo": item.get("Correo"),
        "Rol": item.get("Rol"),
        "Plan": item.get("Plan", {}),
        "Logueo": item.get("Logueo", {})
    }

def usersEntity(items) -> list:
    return [userEntity(item) for item in items]

#recibimos un objeto de tipo user y lo convertimos a un diccionario 
#lista de los usuarios por un array 
