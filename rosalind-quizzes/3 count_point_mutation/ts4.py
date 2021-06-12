#GAGCCTACTAACGGGAT
#CATCGTAATGACGGCCT

#7

s1='GAGCCTACTAACGGGAT'
s2='CATCGTAATGACGGCCT'

import sys
PATH = sys.path[0]+'/data.txt'

def open_file(path):

   f=open(path,'r')
   return f.readlines()
   
   
def check(s):
   s1=s[0]
   s2=s[1]
   c=0
   
   for k in range(len(s1)):
      if s1[k] != s2[k]:
         c+=1
    
   return(c)

s=open_file(PATH)

count=check(s)
print(count)
