##Programa para complementar los Paths con entradas de usuarios

def f_ocgcheck(x):
    if x == "1":
        return '3910'
    else:
        return '3911'


def f_archivo(x):
    if x == '1':
        return '_offline_'
    elif x == '2':
        return '_retry_'
    else:
        return '_indretry_'

def f_busqueda(x):
    if x == '_offline_':
        return 'B04: Group'
    elif x == '_retry_':
        return  'Delivery'
    else:
        return 'L3 Inbound Retry'

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

I_TypeSearch = f_archivo(input("""
Ingrese un tipo de busqueda:

1. offline
2. retry
3. Ind Retry

Valor: """))

OCG_Path = Directorio + I_OCG + Dash + I_Fecha + Formato
Search_Path = Directorio + I_TypeSearch + I_Fecha + Formato2
OpenFile = open(Search_Path, 'x')

ValorBusqueda = f_busqueda(I_TypeSearch)

with open(OCG_Path,"r") as fin, open(Search_Path,"w") as fout:
    string = ValorBusqueda
    for line in fin:
        if string in line:
            fout.write(line)
            try:
                while ValorBusqueda not in line:
                    line = next(fin)
                    fout.write(line)
            except StopIteration:
                pass  # ran out of file to read


