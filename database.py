from pymongo import MongoClient

uri = "mongodb+srv://alexdbuster:iHQMJfHL1AXrYINd@cluster0.xgnrujr.mongodb.net/recipe_db?retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("✅ Conexión exitosa a MongoDB Atlas")
except Exception as e:
    print("❌ Error:", e)
