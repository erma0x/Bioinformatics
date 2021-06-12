#input
# GATGGAACTTGACTACGTAAATT

#output
# GAUGGAACUUGACUACGUAAAUU
import sys

def transcribe(path):
    c=''
    f = open(path, "r")
    for i in f:
       c+=i.replace("T","U")
    return c


PATH =sys.path[0]+"/data.txt"
d=transcribe(PATH)
print(d)
