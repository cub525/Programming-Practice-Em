# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:43:38 2020

@author: EOL
"""

# Python program to conver 
# altered DNA to protein 
  
#inputfile ="DNA.txt" 
#f = open(inputfile, "r") 
#seq = f.read() 
#  
#seq = seq.replace("\n", "")  
#seq = seq.replace("\r", "") 

table = { 
        'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
        'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
        'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
        'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
        'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
        'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
        'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
        'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W' 
    } 

inv_table = {v: k for k, v in table.items()}

def dnatomrna(seq):
    scribe = seq.maketrans('ACTG','UGAC')
    mrna = seq.translate(scribe)
    return mrna

def rnatodna(seq):
    scribe = seq.maketrans('UGAC','ACTG')
    mrna = seq.translate(scribe)
    return mrna

def mrnatotrna(seq):
    scribe = seq.maketrans('ACUG','UGAC')
    mrna = seq.translate(scribe)
    return mrna

def rnatoaa(seq):
    protein ="" 
    if len(seq)%3 == 0: 
        for i in range(0, len(seq), 3): 
            codon = seq[i:i + 3] 
            protein+= table[codon] 
    return protein 

def dnatoaa(seq):
    rna = dnatomrna(seq)
    protein = rnatoaa(rna)
    return protein


def aatorna(aa):
    rna = ''
    for i in aa:
        rna += inv_table[i]
    return rna
if __name__ == '__main__':
    print(dnatoaa('TACCGCTCCGCCGTCGACAATACCACT'))
 