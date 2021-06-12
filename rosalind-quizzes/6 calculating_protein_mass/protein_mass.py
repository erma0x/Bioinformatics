def openfile():
    import sys 
    PATH = sys.path[0]+'/data.txt'
    with open (PATH, "r") as myfile:
        data=myfile.readlines()
        myfile.close()
        return(data)

def create_dict():
    import sys
    d={} # my dict
    PATH = sys.path[0]+'/mass_protein.txt'
    myfile = open(PATH,'r')
    for line in myfile:
        row = line.replace('   ','')
        row = row.split()
        d[row[0]] = float(row[1])

    print(d)
    return(d)

def format_str(mylist):
    sequence_string = mylist[0].replace('\n','')
    return sequence_string 

def mass_calculator(sequence,dict_mass):
    mass = 0
    for i in range(len(sequence)):
        mass += float(dict_mass[sequence[i]])
    return mass


data = openfile()
data = format_str(data)
diz = create_dict()
result = mass_calculator(data,diz)
print(round(result,3))