standardGeneticCode = {
          'UUU':'Phe', 'UUC':'Phe', 'UCU':'Ser', 'UCC':'Ser',
          'UAU':'Tyr', 'UAC':'Tyr', 'UGU':'Cys', 'UGC':'Cys',
          'UUA':'Leu', 'UCA':'Ser', 'UAA':None,  'UGA':None,
          'UUG':'Leu', 'UCG':'Ser', 'UAG':None,  'UGG':'Trp',
          'CUU':'Leu', 'CUC':'Leu', 'CCU':'Pro', 'CCC':'Pro',
          'CAU':'His', 'CAC':'His', 'CGU':'Arg', 'CGC':'Arg',
          'CUA':'Leu', 'CUG':'Leu', 'CCA':'Pro', 'CCG':'Pro',
          'CAA':'Gln', 'CAG':'Gln', 'CGA':'Arg', 'CGG':'Arg',
          'AUU':'Ile', 'AUC':'Ile', 'ACU':'Thr', 'ACC':'Thr',
          'AAU':'Asn', 'AAC':'Asn', 'AGU':'Ser', 'AGC':'Ser',
          'AUA':'Ile', 'ACA':'Thr', 'AAA':'Lys', 'AGA':'Arg',
          'AUG':'Met', 'ACG':'Thr', 'AAG':'Lys', 'AGG':'Arg',
          'GUU':'Val', 'GUC':'Val', 'GCU':'Ala', 'GCC':'Ala',
          'GAU':'Asp', 'GAC':'Asp', 'GGU':'Gly', 'GGC':'Gly',
          'GUA':'Val', 'GUG':'Val', 'GCA':'Ala', 'GCG':'Ala',
          'GAA':'Glu', 'GAG':'Glu', 'GGA':'Gly', 'GGG':'Gly'}

# Write a function that translates a RNA sequence into a sequence of amino acids.
# The function should take 2 arguments, a RNA sequence and a dictionary that defines the standard genetic code.

def translate(rna, code):
    codon_size = 3
    assert len(rna)%codon_size == 0, "RNA string length must be divisible by 3!"
    codons = []
    for i in range(0, len(rna), codon_size):
        codons.append(rna[i:i+codon_size].upper())
    return "".join(map(lambda x: code[x], codons))

print translate('UUAUACAGU', standardGeneticCode)
print translate('UUAUACAG', standardGeneticCode)