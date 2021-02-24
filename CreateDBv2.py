import pymongo
DBClient = pymongo.MongoClient('mongodb://localhost:27017/')
DBIClient = DBClient["HXEmployers"]
MyDict = {
    "UserID": 900001
    "FName": "Hector",
    "LName": "Lara",
    "Job": "NOC Engineer Jr.",
    "JobID":"NOCENG"
}
CollUsers = DBIClient["Employers"]
MyDict_Input = CollUsers.insert_one(MyDict)

x = CollUsers.find_one()
print(x)