import urllib.parse
from pymongo import MongoClient

username = 'bibekwiwek54'
password = 'Pokhara@123'

encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)


uri = "mongodb+srv://{encoded_username}:{encoded_password}@cluster0.r3ms4pa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client['Next_Career']