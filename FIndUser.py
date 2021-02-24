import pymongo
DBClient = pymongo.MongoClient('mongodb://localhost:27017/')
DBIClient = DBClient["HXEmployers"]
CollUsers = DBIClient["Employers"]
Nombre = input('Ingresa el nombre de busqueda: ')
MyQuery = {'FName': Nombre}
UserID_LST = CollUsers.find(MyQuery).sort('UserID').distinct('UserID')
UserID_INT = UserID_LST[0]
print(UserID_INT)
print(type(UserID_INT))