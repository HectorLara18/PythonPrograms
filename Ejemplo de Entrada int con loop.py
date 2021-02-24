##Ejemplo 1 
##Entrada donde tiene que ser un numero 

def f_int(x):
    try:
        return int(x)
    except ValueError:
        return 'Error'

E1 = 'cero'
E2 = 'cero'

while type(E1) != int:
    E1 = f_int(input("Ingrese el valor 1: "))


while type(E1) != int:
    E1 = f_int(input("Ingrese el valor 1: "))