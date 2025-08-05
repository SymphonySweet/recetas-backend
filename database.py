from pymongo import MongoClient
import os

# Lee la URI de MongoDB desde variable de entorno o usa la local por defecto
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://alexdbuster:iHQMJfHL1AXrYINd@cluster0.xgnrujr.mongodb.net/recipe_db?retryWrites=true&w=majority")

# Conexión al cluster de MongoDB Atlas
client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)

# Selecciona la base de datos 'recipe_db'
db = client["recipe_db"]

# Verifica conexión (opcional, útil en local)
try:
    client.admin.command("ping")
    print("✅ Conexión exitosa a MongoDB Atlas")
except Exception as e:
    print("❌ Error de conexión a MongoDB:", e)

