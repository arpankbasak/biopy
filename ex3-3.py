def mean2(args):
    return float(sum(args))/len(args)

def weight(dna, molecule='dna'):
    weightConversions = {}
    if (molecule == 'dna'):
        weightConversions = {'A': 331, 'C': 307, 'G':347, 'T': 306}
    elif(molecule == 'rna'):
        weightConversions = {'A': 347, 'C': 323, 'G':363, 'U': 324}
    else:
        raise Exception("Unknown molecule type " + molecule)
    weights = map(lambda x: weightConversions.get(x, mean2(weightConversions.values())), list(dna))
    return sum(weights)

print weight("AATAGANAGATAGANCCCATAC")
print weight("AAUUCCGCCUAAAUCUAUCUA", 'rna')
# print weight("AAUUCCGCCUAAAUCUAUCUA", 'dunno')
