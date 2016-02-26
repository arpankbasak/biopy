import Bio as bp
from Bio.Seq import Seq
from Bio import SeqIO, Alphabet
from Bio.Alphabet import generic_dna
from Bio.Alphabet import IUPAC
import numpy as np
import pandas as pn
#
# my_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
# protein_seq = Seq("EVRNAK", IUPAC.protein)
# print my_seq + protein_seq


# for seq_record in SeqIO.parse("../data/ls_orchid.fasta", "fasta"):
#     print(seq_record.id)
#     print(repr(seq_record.seq))
#     print(len(seq_record))
#
# for seq_record in SeqIO.parse("../data/ls_orchid.gbk", "genbank"):
#     print(seq_record.id)
#     print(repr(seq_record.seq))
#     print(len(seq_record))

# sequences = SeqIO.parse("../data/ls_orchid.fasta", "fasta", alphabet=IUPAC.unambiguous_dna)
# my_dna = sequences.next()
#
# my_rna = my_dna.seq.transcribe()
# my_protein = my_rna.translate()
# print "Protein alphabet is", my_protein.alphabet
#
# gene = Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA" + \
#             "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT" + \
#             "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT" + \
#             "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT" + \
#             "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA",
#             generic_dna)
#
# trans1 = gene.translate(table="Bacterial")
# trans2 = gene.translate(table="Bacterial", to_stop=True)
# trans3 = gene.translate(table="Bacterial", cds=True)
gene_start = 26087281
my_snp = 845
snp_on_chromosome = gene_start + my_snp
# print snp_on_chromosome
# //NC_000003.12
# record = SeqIO.read("../data/NC_005816.gb", "genbank")
record = SeqIO.read("../data/NC_000006.12.gb", "genbank")
# for feature in record.features:
#     if my_snp in feature:
#         print("%s %s" % (feature.type, feature))

# print len(record.seq)
# sub_record = record[:my_snp+7000]
# print sub_record

# rev = record.reverse_complement()
#
# print len(rev.features)
# print len(record.features)
# print record.annotations

#TODO use the GeneId annotation from the above file to looks for SNPs

from Bio import Entrez
Entrez.email = "brendan.lawlor@gmail.com"     # Always tell NCBI who you are
# handle = Entrez.einfo()
# handle = Entrez.esearch(db="pubmed", term="rs1800562") #rs1800562
# handle = Entrez.esearch(db="snp", term="rs1800562") #rs1800562
# record = Entrez.read(handle)
# print "\n".join(record['DbList'])
# print record
ids= ['17530654', '4134660', '1800562']
for id in ids:
    handle = Entrez.efetch(db="snp", id=id)
    with open("../data/snp" + id + ".txt", "w") as output:
        output.write(handle.read())
# print handle.read()
