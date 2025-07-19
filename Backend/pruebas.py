from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://sergiojairceron:1l1KR3S4W1@cluster0.03zbm47.mongodb.net/Reporteria?retryWrites=true&w=majority",
    tls=True,
    tlsAllowInvalidCertificates=True
)

try:
    db = client["Reporteria"]
    print("Colecciones:", db.list_collection_names())
    print("Usuarios:", list(db["Usuarios"].find()))
except Exception as e:
    print("ERROR DE CONEXIÓN:", e)
