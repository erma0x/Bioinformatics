
#input
#AAAACCCGGT

#output
#ACCGGGTTTT

import sys

def transcribe(path):
    """python2"""
    
    from string import maketrans
    
    c=''
    f = open(path, "r")
    intab = "ACGT"
    outtab = "TGCA"
    trantab = maketrans(intab, outtab)

    string = f.readline()
    
    tranlated = string.translate(trantab)
    reverse_translated = tranlated[::-1].replace('\n','')

    print(reverse_translated)
    return (reverse_translated)
 
PATH =sys.path[0]+"/data.txt"
rv=transcribe(PATH)

