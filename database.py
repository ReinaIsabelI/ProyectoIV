from pymongo import mongo_client
import certifi

MONGO_URI = '#AQUI VA LA RUTA DEL LOCALHOST, LUEGO TE PASO UN TUTORIAL DE COMO LA SACAS DE MONGO'
ca = certifi.where()

def dbConnection():
    try:
        client = mongo_client(MONGO_URI, tlsCAFile=ca)
        db = client["aqui colocas el nombre de la base de datos, pero como ciempre me equivoco mejor ponla tu"]
    except ConnectionError:
        print('ERROR DE CONEXION CON LA BASE DE DATOS')
    return db