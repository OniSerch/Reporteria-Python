#esquema de que va a tener la base de datos
#coleccion de usuarios importamos las rutas
#definimos una funcion el cual sera objeto que nos regresa un diccionario 
def userEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "usuario": item.get("usuario"),
        "email": item.get("email"),
        "pass_hash": item.get("pass_hash"),
        "rol": item.get("rol"),
        "pago": item.get("pago", False),
        "activo": item.get("activo", True),
        "plan": item.get("plan", {}),
        "logueo": item.get("logueo", {})
    }

def usersEntity(items) -> list:
    return [userEntity(item) for item in items]

#recibimos un objeto de tipo user y lo convertimos a un diccionario 
#lista de los usuarios por un array 
