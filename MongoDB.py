# import MongoClient 
from pymongo import MongoClient 
  
  
# Creating a client 
client = MongoClient('localhost', 27017) 
  
# Greating a database name GFG 
db = client['OCG-DB'] 
print("Database is created !!")
