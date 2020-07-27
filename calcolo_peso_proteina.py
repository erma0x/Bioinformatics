#ritorna la somma del peso 

volume_di = {
    "A":  67.0, "C":  86.0, "D":  91.0,
    "E": 109.0, "F": 135.0, "G":  48.0,
    "H": 118.0, "I": 124.0, "K": 135.0,
    "L": 124.0, "M": 124.0, "N":  96.0,
    "P":  90.0, "Q": 114.0, "R": 148.0,
    "S":  73.0, "T":  93.0, "V": 105.0,
    "W": 163.0, "Y": 141.0,
}

fasta = """>1BA4:A|PDBID|CHAIN|SEQUEN
DAEFRHDSGYEVHHQKLVFFAEDVGSNKGAIIGLMVGGVVVVVV"""

fasta2=fasta.split()
fasta2=fasta2[1]
fasta2=list(fasta2)
somma=0
a=volume_di.values()
c=list(volume_di.items())
a=list(a)

for k in c:
    for g in fasta2:
        if k[0]==g:
            valore=k[1]
            somma=somma+valore
print (somma)
