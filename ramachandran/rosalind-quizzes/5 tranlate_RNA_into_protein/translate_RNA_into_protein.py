map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"", "UAG":"",
    "UGU":"C", "UGC":"C", "UGA":"", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def openfile():
    from sys import path
    PATH = path[0]+'/data.txt'
    with open (PATH, "r") as myfile:
        data=myfile.readlines()
        myfile.close()
        return(data)

def format_str(mylist):
    sequence_string = mylist[0].replace('\n','')
    return sequence_string 

def tranlate_RNA_protein(table_conversion):
    sequence = openfile()
    protein=''
    sequence = format_str(sequence)
    for i in range(0,len(sequence)-3,3):
        protein += sequence[i:i+3].replace(sequence[i:i+3], table_conversion[sequence[i:i+3]].upper())
    return protein


result = tranlate_RNA_protein(map)
print(result)
