from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://eajun:eajun030802@cluster0.ktfe47o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    # Create a new client and connect to the server
    client = MongoClient(uri)
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
