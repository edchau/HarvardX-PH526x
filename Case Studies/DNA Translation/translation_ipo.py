#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 21:37:02 2018

@author: Edward
"""

#www.ncbi.nlm.nih.gov

#inputfile = "dna.txt"
#f = open(inputfile, "r")
#seq = f.read()
#seq = seq.replace("\n", "")
#seq = seq.replace("\r", "")


def read_seq(inputfile):
    """
    Reads and returns the input sequence with special
    characters removed.
    """
    
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq
    
#inputfile = "dna.txt"
#prt = read_seq("protein.txt")
#dna = read_seq("dna.txt")
    #CDS (Seq Start and End): (21..938), index starts at 1
#translate(dna[20:938])
#translate(dna[20:935]) without stop codon

def translate(seq):     
    """
    Translate a string containing a nucleotide sequence into a string
    containing the corresponding sequence of amino acids. Nucleotides are
    translated in triplets using the table dictionary; each amino acid
    is encoded with a stirng of length 1.
    """
    
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    protein = ""
    #check that seq length is div by 3
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            #extract single codon
            protein += table[codon] 
            #look up codon and store the result
            
    return protein