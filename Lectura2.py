Path= "C:\\Users\hecto\Documents\Programación\PruebaLectura.txt"
Path2= "C:\\Users\hecto\Documents\Programación\PruebaCreación.txt"
f = open(Path,"r")
f2 = open(Path2,"w")
print(f.read())

for line in Path:
    Path2.write(line)
Path.close()
Path2.close()
