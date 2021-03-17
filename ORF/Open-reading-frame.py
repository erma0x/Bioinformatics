sequenza = "ATGGCGCCCGUGGCACCGUUAGAACUUAGGACAUUAGGGA"
c1=list(range(0, len(sequenza), 3))
c2=list(range(1, len(sequenza), 3))
c3=list(range(2, len(sequenza), 3))
contastop1,contastop2,contastop3=0,0,0

orf1,orf2,orf3=[],[],[]
for i in c1:
    tripletta=sequenza[i:i+3]
    orf1.append(tripletta)
for i in c2:
    tripletta=sequenza[i:i+3]
    orf2.append(tripletta)
for i in c3:
    tripletta=sequenza[i:i+3]
    orf3.append(tripletta)
contastop=0
stop=['UAG','UGA','UGG']
for i in orf1:
    if i in stop:
        contastop1+=1
print('stop codon trovati in ORF1',contastop1)

for i in orf2:
    if i in stop:
        contastop2+=1
print('stop codon trovati in ORF2',contastop2)

for i in orf3:
    if i in stop:
        contastop3+=1
print('stop codon trovati in ORF3',contastop3)
l=[contastop1,contastop2,contastop3]
min=l[0]
for i in l:
    if i<min:
        min=i
if min==contastop1:
    probabile='orf1'
elif min==contastop2:
    probabile='orf2'
else:
    probabile='orf3'

print('sono stati trovati ', min ,' stop codon nella seq piu probabile che ', probabile)
