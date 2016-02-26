dna = {"A": "Adenine", "C": "Cytosine", "G": "Guanine", "T": "Thymine"}

c = 'TGT'
l = 'ATT'
y = 'TAT'
s = 'TCT'

translation = {"GTT": "V", "GCA": "A", "CCA": "P", "CAA": "Q", "CCG": "P"}

seq = "GTT GCA CCA CAA CCG"

codons = seq.split(" ")

from Bio.Seq import Seq
from Bio import SeqIO, Alphabet
from Bio.Alphabet import IUPAC

sequences = SeqIO.parse("./data/lysozyme.fasta", "fasta", alphabet=IUPAC.protein)
lysozyme_seq = sequences.next()

residues = list(lysozyme_seq)
abundances = {}
for r in residues:
    abundances[r] = 1 + abundances.get(r, 0)

keys = abundances.keys()
keys.sort()
for k in keys:
    print "There are %d instances of residue %s" % (abundances[k], k)