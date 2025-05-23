from Bio import SeqIO
import sys


def removeN(file):
    '''
    Function that parses the fasta file to find any missing sequences (denoted by "N" instead of usual A,C,T,G)
        Create a new fasta file that contains all of the sequences without any missing data from positions 21-420
    :param file:  string, file path to the working directory
    :return: None
    '''
    if "V" in file:
        n = open(f"{file[:79]}-N {file[80:-10]}.fasta", "w")
    else:
        n = open(f"{file[:78]}-N {file[79:-10]}.fasta", "w")

    count = 0
    length = 0

    for rec in SeqIO.parse(file, "fasta"):
        length += 1
        numN = rec.seq.count("N", 21, 421)
        hasN = numN > 0
        if not hasN:
            SeqIO.write(rec, n, "fasta-2line")
            count+=1

    print("Total rows: ", length)
    print("Rows with no N: ", count)


def main():
    removeN(sys.argv[1])

if __name__=="__main__":
    main()