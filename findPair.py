from Bio import SeqIO
from collections import defaultdict
import sys

def findPair(file):
    '''
    Function that parses the fasta file to find any duplicate sequence names and separate non-main sequences into their own file
    :param file:  string, file path to the working directory
    :return: None    
    '''
    single_output = open(f"{file[:-6]}_single.fasta", "w")
    pair_output = open(f"{file[:-6]}_pair.fasta", "w")


    barcodes = defaultdict(list)
    for rec in SeqIO.parse(file, "fasta"):
        header = rec.id.split("_contig")
        barcode = header[0]
        barcodes[barcode].append(rec)


    count = 0
    for rec in barcodes.values():
        if (len(rec)==1):
            SeqIO.write(rec, single_output, "fasta-2line")
        else:
            SeqIO.write(rec, pair_output, "fasta-2line")
            count += 1
    print("Number of pairs:", count)

        
def main():
    findPair("All.fasta")
    # findPair(sys.argv[1])

if __name__=="__main__":
    main()