# Write a function that counts the number of each base found in a DNA sequence.
# Return the result as a tuple of 4 numbers representing the counts of each base A, C, G and T.

def countBases(dna):
    c = 0
    a = 0
    t = 0
    g = 0
    for base in list(dna):
        if base == 'c':
            c += 1
        elif base == 'a':
            a += 1
        elif base == 't':
            t += 1
        elif base == 'g':
            g += 1
    return (a,c,g,t)


print countBases("agagatagatccctcagtcgatcgag")

def countBases2(dna):
    baseMap = {}
    for base in list(dna):
        baseMap[base] = 1+baseMap.get(base, 0)
    return baseMap['a'], baseMap['c'], baseMap['g'], baseMap['t'],

print countBases2("agagatagatccctcagtcgatcgag")


pairs = {'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}
def reverseComplement(dna):
    complement = map(lambda b: pairs[b], list(dna.lower()))
    return "".join(list(reversed(complement)))


print reverseComplement("agagatagatccctcagtcgatcgag")
