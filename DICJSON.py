#Diccionario + json 
import json

User1 = {'FName':'Hector',
         'LName':'Lara',
         'Job':'Development',
         'Number':'0001'}

JUser1 = json.dumps(User1)

print('esto es un diccionario dwe python:')
print(User1)
print('esto es un mensaje en formato JSON:')
print(JUser1)
