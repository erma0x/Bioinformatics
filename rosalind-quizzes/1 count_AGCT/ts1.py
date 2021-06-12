path ="/home/jack/Desktop/rosalind_dna.txt"

def check(path):
   #'A', 'C', 'G','T' 
   f = open(path, "r")
   c=0
   for j in f.readlines():
      print( j.count('A'),j.count('C'),j.count('G'),j.count('T') )
   
check(path)

