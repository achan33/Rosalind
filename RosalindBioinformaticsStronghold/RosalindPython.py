#!/usr/bin/env python3

from collections import Counter
import collections

#given a DNA string, give frequency of A C G T respectively
def count_ACGT(file):
    with open(file, 'r') as infile, open('outfile4.txt' , 'w') as outfile:
        #read in string sequence and break down into char(nt)
        string = infile.readline()
        res = []
        res[::] = string
        #use counter to count freq
        
        #sort dictionary v
        for key in sorted(v=Counter(res)):
            outfile.write("%s: %s" % (key, v[key]))
            #print("%s : %s" % (key,v[key]))

#another method to count DNA
def count_nt(file):
    with open(file, 'r') as infile:
        s = infile.readline()
        return s.count('A') , s.count('G') , s.count('C') , s.count('T')

#transcribe dna to RNA replace T with U
def dna_to_rna(file):
    with open(file, 'r') as infile , open('outfile2.txt' ,'w') as outfile:
        string = infile.readline()
        string = string.replace('T','U')
        outfile.write(string)

#give the complment of dna
def complement_dna(file):
    comp = { 'A':'T' , 'C' :'G' , 'T' :'A' , 'G' :'C' }
    with open (file , 'r') as infile, open ('outfile3.txt' , 'w') as outfile:
        line= infile.readline()
        line = line.rstrip()
        test = "GTGATAGAC"
        comp_t = ""
        for s in line:
            comp_t += comp[s]
        outfile.write(comp_t)

#give reverse complement same as previous method but with [::-1]
def rev_comp_dna(file):
    comp = { 'A':'T' , 'C' :'G' , 'T' :'A' , 'G' :'C' }
    with open (file , 'r') as infile, open ('outfile3.txt' , 'w') as outfile:
        line= infile.readline()
        line = line.rstrip()
        comp_t = ""
        for s in line:
            comp_t += comp[s]
        outfile.write(comp_t[::-1])

#takes in string sequence instead for rev comp
def rev_dna_string(string):
    string = string.rstrip()
    comp = { 'A':'T' , 'C' :'G' , 'T' :'A' , 'G' :'C' }
    return "".join(comp[s] for s in string[::-1])


def main():

    #v = count('rosdna1.txt')
    #print(v)
    #dna_to_rna('rosadna2.txt')
    #rev_comp_dna('rosalind_revc.txt')
    

if __name__ == '__main__':
    main()
else:
    print("This program no work") 
