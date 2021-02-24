import pymongo
DBClient = pymongo.MongoClient('mongodb://localhost:27017/')
DBIClient = DBClient["HXEmployers"]
CollUsers = DBIClient["Employers"]
UserID_LST = CollUsers.find().sort('UserID', -1)
print(UserID_LST)
for x in UserID_LST:
    print(x)