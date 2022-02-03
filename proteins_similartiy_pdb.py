#!/usr/bin/env/ python3
"""

Take in input 2 proteins from pdb and search for similartiy 
It use .pdb file format for finding the atoms coordinates and filtering.

Usage $ python3 script.py pdb_file_A pdb_file_B [A-B] [A-B]
e.g.  $ python3 script.py 3ZCF.pdb 3O20.pdb A A
Chain are Alpha Helixes or Beta Sheets
"""

import sys
from Bio.SVDSuperimposer import SVDSuperimposer
import numpy as np

def get_list(num_aa):
    """
    get list of position
    of the amino acid analyzed
    that are present in the pdb file
    """
    rlist = []
    v = num_aa.split('-')
    
    if len(v) == 2:
        rlist = range(int(v[0]), int(v[1])+1)
        rlist=[str(i) for i in rlist]
    else:
        sys.stderr.write("ERROR: Incorrect amino acid list. ")
        sys.exit(1)

    return(rlist)


def get_RMSD(list_atoms1,list_atoms2):
    if len(list_atoms1)!=len(list_atoms1):
        sys.stderr.write("ERROR: Different number of elements. ")
        sys.exit(3)
    
    svd = SVDSuperimposer()
    svd.set(np.array(list_atoms1),np.array(list_atoms2) )
    svd.run()
    rmsd = svd.get_rms()
    print(rmsd)



def parse_pdb(pdbfile,chain, rlist, atom="CA"):
    
    list_chain_atoms = []

    f = open(pdbfile)

    for line in f:
        line = line.rstrip()

        # __________ FILTERS _____________
        if line.find("ATOM") != 0: continue
        # return only line with 'ATOM'
        # in the position 0
            
        if len(line) < 78: continue
        # take only ATOM coordinates information

        if line[21] != chain: continue
        # take only our chain of interest
        
        if line[11:16].strip() != atom: continue
        # take only the atom in input

        if line[16]!=" " and line[16]!="A": continue

        aa_pos = line[22:26].strip()

        if aa_pos not in rlist: continue
        # if the amino acid number of the C alpha
        # you are reading, is not providing the 
        # number that you needed

        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        # print(aa_pos, [x,y,z])

        list_chain_atoms.append([x,y,z])


    if len(list_chain_atoms) == 0:
        sys.stderr.write("ERROR: Incorrect amino acid selection. ")
        sys.exit(2)  
    
    return list_chain_atoms

if __name__ =="__main__":
    pdb1 = sys.argv[1]
    pdb2 = sys.argv[2]
    ch1 = sys.argv[3]
    ch2 = sys.argv[4]
    rlist1 = get_list(sys.argv[5])
    rlist2 = get_list(sys.argv[6])
    list_aa1 = parse_pdb(pdb1,ch1, rlist1)
    list_aa2 = parse_pdb(pdb2,ch2, rlist2)

    #print(list_aa1,list_aa2)
    get_RMSD(list_aa1,list_aa2)
