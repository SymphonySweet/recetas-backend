from pymongo import MongoClient
import os

# Lee la URI desde variable de entorno o usa la de Atlas como fallback
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://alexdbuster:iHQMJfHL1AXrYINd@cluster0.xgnrujr.mongodb.net/recipe_db?retryWrites=true&w=majority&tls=true"
)

# Conexión al cluster de MongoDB Atlas con TLS válido y más tiempo de espera
client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsAllowInvalidCertificates=False,  # No aceptar certificados inválidos
    serverSelectionTimeoutMS=30000      # 30 segundos de espera
)

# Selecciona la base de datos
db = client["recipe_db"]

# Verifica conexión (opcional)
try:
    client.admin.command("ping")
    print("✅ Conexión exitosa a MongoDB Atlas con TLS 1.2")
except Exception as e:
    print("❌ Error de conexión a MongoDB:", e)
