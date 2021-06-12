# calculate GC content in Rosalind format

def openfile():
    import sys 
    PATH = sys.path[0]+'/data.txt'
    with open (PATH, "r") as myfile:
        
        string='' # string = sequence DNA/RNA
        diz={} # key = rosalinID  | value = sequence DNA/RNA

        for i in myfile.readlines():
            
            if 'Rosalind' in i:
                ID = i.replace('\n','').replace('>','')
            
            else:
                string += i
                diz[ID] = string.replace('\n','') 

        myfile.close()
        return(diz)

def CG_contnent(mydiz):
    new_diz = {} # Example:  {'Rosalind_6404' : 0.5375}
    for k,v in mydiz.items():
        C_count, G_count = 0, 0
        C_count += v.count('C')
        G_count += v.count('G')
        GC = (C_count+G_count) / len(v)
        new_diz[k]=GC
    
    return get_max(new_diz)


def get_max(diz):
    inverse = [(value, key) for key, value in diz.items()]
    return max(inverse)

data = openfile()
result=CG_contnent(data)

print(' ID sequence : ',result[1])
print(' GC % : ',result[0])

