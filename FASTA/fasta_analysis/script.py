

file_path = '/home/jack/Desktop/biotest/sequences.fasta'

def openFASTA(path):
	a = open(path).readlines()
	dna = ' '.join( a[1:] )
	dna = dna.replace('\n',' ')
	return dna




# gccontent . py
def GCcontent( instr , window =128 , step =32 ) :
    answ = []
    for i in range ( 0 , len ( instr ), step):
        cut = instr [ i : i + window ]. lower ()
        a = cut.count( 'a' )
        g = cut.count( 'g' )
        c = cut.count( 'c' )
        t = cut.count( 't' )
        ratio = float(( c + g ) /( a + c + g + t ))
        answ.append( ratio )
    return answ




def Complement( st ) :
	table = st.maketrans('ACGT','TGCA')
	st1 = st.translate(table) # swap ACTG
	#st1 = st1 [::-1] # reverse string
	return st1 



def CheckStartStop( dna , bounds ) :
    N = len(bounds)
    bad = []
    for i in range(N) :
        start , stop , cflag = bounds[i]
        cut = dna[ start-1: stop ]
        if cflag:
            cut = gb.Complement( cut )
        m3 = ( stop-( start-1) ) % 3
        startcodon = cut[:3]
        stopcodon = cut[-3:]
        if m3 ==0 and ( startcodon == ' atg ' or startcodon == ' gtg ' 
            or startcodon == ' ttg ' ) and ( stopcodon == ' tag ' or 
            stopcodon == ' taa ' or stopcodon == ' tga ' ) :
            pass
        else :
            bad.append( ( start , stop , cflag ) )
    return bad

def print_out(obj,name):
    print('\n')
    print('-type {0} '.format(name),type(obj))
    print('-len {0} '.format(name), len(obj))
    print('-example {0} : '.format(name), obj[:10])
    print('\n')

DNA = openFASTA(file_path)
print_out(DNA,'DNA')


gc = GCcontent( DNA ,8 ,4)
print_out(gc,'GC')


complement = Complement(DNA)
print_out(complement,'complement')

bad = CheckStartStop( DNA , bounds )
print_out(bad,'bad')
