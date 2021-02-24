##Programa para lectura de Log de OCG

Path= "C:\\Users\hecto\Documents\KCSM Archivos\CTC\ArchivosOCG\OCG3910_20200908.log"
Path2= "C:\\Users\hecto\Documents\Programación\offline.txt"

with open(Path,"r") as fin, open(Path2,"w") as fout:
    string = input("Enter the String:")
    for line in fin:
        if string in line:
            fout.write(line)
            try:
                while 'offline' not in line:
                    line = next(fin)
                    fout.write(line)
            except StopIteration:
                pass  # ran out of file to read