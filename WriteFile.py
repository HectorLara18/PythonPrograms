import os

if os.path.exists("TESTFile4.txt"):
    os.remove("TESTFile4.txt")
    print("Archivo Removido")
else:
    print("Archivo No Existe")

x = open("TESTFile4.txt",'x')
y = "Esto es una prueba de escritura"
x.write(y)
x.close()
x = open("TESTFile4.txt","r")
print(x.read())