# Return the sum of the weights 

def fasta_weigth(fasta_string):
    
    weight = {
    "A":  67.0, "C":  86.0, "D":  91.0,
    "E": 109.0, "F": 135.0, "G":  48.0,
    "H": 118.0, "I": 124.0, "K": 135.0,
    "L": 124.0, "M": 124.0, "N":  96.0,
    "P":  90.0, "Q": 114.0, "R": 148.0,
    "S":  73.0, "T":  93.0, "V": 105.0,
    "W": 163.0, "Y": 141.0}
    
    sum=0

    fasta_modified=fasta_string.split()
    fasta_modified=list(fasta_modified[1])
    
    weights = list(weight.items())
    
    for Win weights:
        for letter in fasta_modified:
            if W[0] == letter :
                sum = sum + W[1]
                
    return(sum)


FASTA_string = """>1BA4:A|PDBID|CHAIN|SEQUEN
DAEFRHDSGYEVHHQKLVFFAEDVGSNKGAIIGLMVGGVVVVVV"""

sum=fasta_weigth(FASTA_string)
print(sum)
    
