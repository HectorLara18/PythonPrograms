Lista = []
x = 'inicio'

while  x != 'fin':
    x = input("Ingrese un dato a la lista:")
    Lista.append(x)
    if x == 'fin':
        break
    elif len(Lista) == 5:
        print("no se puede agregar mas numeros")
        break



if 'fin' in Lista:
    Lista.remove('fin')

print(Lista)
print(len(Lista))