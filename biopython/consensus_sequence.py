from Bio import SeqUtils

consensus = "RGWYV"

sequence = "CGTAGCTAGCTCAGAGCAGGGACACGTGCTAGCAACAGCGCT"

SeqUtils.nt_search(sequence,consensus)

