def mean(x,y):
    return (float(x+y))/2

print mean(1,2)

print mean(1.3, 5.003)

def mean2(args):
    return float(sum(args))/len(args)

print mean2([1,2,3])

print mean2([1.0, 5e2, -54])


def weight(dna):
    weightConversions = {'A': 331, 'C': 307, 'G':347, 'T': 306}
    weights = map(lambda x: weightConversions.get(x, mean2(weightConversions.values())), list(dna))
    return sum(weights)

print weight("AATAGANAGATAGANCCCATAC")