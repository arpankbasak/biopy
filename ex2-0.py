my_age = 46
seans_age = 81

if (my_age < seans_age):
    print "I'm younger"
elif (my_age > seans_age):
    print "I'm older"
else:
    print "We're the same age"

dna = "ATGGCGGTCGAATAG"
stop_codons = ["TAG", "TAA", "TGA"]
for stop_codon in stop_codons:
    if stop_codon in dna:
        print "Yes"
        continue

