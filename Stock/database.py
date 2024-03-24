from pymongo import MongoClient

# MongoDB Compass connection string with escaped username and password
connection_string = "mongodb+srv://eajun:eajun030802@cluster0.ktfe47o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Initialize the MongoClient with your connection string
client = MongoClient(connection_string)

db = client.Eajun
collection = db["textData"]

# Perform a text search query
search_query = "Who"  # Simple search query for testing
search_result = collection.find({"$text": {"$search": search_query}})

matching_count = collection.count_documents({"$text": {"$search": search_query}})

if matching_count > 0:
    for result in search_result:
        print(result)
else:
    print("No matching documents found for the search query.")
