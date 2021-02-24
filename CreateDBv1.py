import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["Customers"]

mydict = {
    "Name": "Raul",
    "Last": "Lara",
    "Company": "A&D"
}
x = mycol.insert_one(mydict)
MyDBs = myclient.list_database_names()

print(MyDBs)