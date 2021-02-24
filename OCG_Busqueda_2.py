##Programa para complementar los Paths con entradas de usuarios

def f_ocgcheck(x):
    if x == "1":
        return '3910'
    else:
        return '3911'


Directorio = "C:\\Users\hecto\Documents\KCSMArchivos\CTC\ArchivosOCG\OCG"
Dash = "_"
Formato = ".log"
Formato2 = ".txt"

I_OCG = f_ocgcheck(input("""
Ingrese un valor para escoger el archivo de OCG:

1. Para OCG1
2. Para OCG2


Valor: """))
I_Fecha = input("Ingrese la fecha en formayo yyyymmdd:")

C_Offline = '_offline_'
C_Retry = '_retry_'
C_IndRetry = '_indretry_'

OCG_Path = Directorio + I_OCG + Dash + I_Fecha + Formato
Search_Path1 = Directorio + I_OCG + C_Offline + I_Fecha + Formato2
Search_Path2 = Directorio + I_OCG + C_Retry + I_Fecha + Formato2
Search_Path3 = Directorio + I_OCG + C_IndRetry + I_Fecha + Formato2
OpenFile1 = open(Search_Path1, 'x')
OpenFile2 = open(Search_Path2, 'x')
OpenFile3 = open(Search_Path3, 'x')

VBusqueda1 = 'B04: Group'
VBusqueda2 = 'Delivery'
VBusqueda3 = 'L3 Inbound Retry'

with open(OCG_Path, "r") as fin, open(Search_Path1, "w") as fout:
    string = VBusqueda1
    for line in fin:
        if string in line:
            fout.write(line)
            try:
                while VBusqueda1 not in line:
                    line = next(fin)
                    fout.write(line)
            except StopIteration:
                pass  # ran out of file to read

print(Search_Path1 +  " completado")

with open(OCG_Path, "r") as fin, open(Search_Path2, "w") as fout:
    string = VBusqueda2
    for line in fin:
        if string in line:
            fout.write(line)
            try:
                while VBusqueda2 not in line:
                    line = next(fin)
                    fout.write(line)
            except StopIteration:
                pass  # ran out of file to read

print(Search_Path2 + " completado")

with open(OCG_Path, "r") as fin, open(Search_Path3, "w") as fout:
    string = VBusqueda3
    for line in fin:
        if string in line:
            fout.write(line)
            try:
                while VBusqueda3 not in line:
                    line = next(fin)
                    fout.write(line)
            except StopIteration:
                pass  # ran out of file to read

print(Search_Path3 + " completado")

