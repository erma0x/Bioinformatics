
# Return the sum of the weights in KDa 
# of the FASTA protein. 
# Do not use for multiple 
# sequences in the same file

import argparse
import fileinput

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()

FASTA_string=args.file.readlines()

def fasta_weigth(fasta_string):
    
    weight = {
    "A":  67.0, "C":  86.0, "D":  91.0,
    "E": 109.0, "F": 135.0, "G":  48.0,
    "H": 118.0, "I": 124.0, "K": 135.0,
    "L": 124.0, "M": 124.0, "N":  96.0,
    "P":  90.0, "Q": 114.0, "R": 148.0,
    "S":  73.0, "T":  93.0, "V": 105.0,
    "W": 163.0, "Y": 141.0}
    
    sum_=0
    
    for row in fasta_string: 
    	if '>' in row: # without index
    		pass
    	else:             
            for letter_fasta in row: # for each letter in FASTA row
                for W in weight.items(): # for each items in dictionary weight
                    if W[0].upper() == letter_fasta: # if letter in Dictionary
                        sum_ = sum_ + W[1]
    sum_=round(sum_)
    print(' protein weight : {0} KDa'.format(sum_))                            
    
fasta_weigth(FASTA_string)

    


        

