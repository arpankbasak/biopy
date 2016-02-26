bases = "AGTCCTAGATGAAAG"
permitted = "ATCG"
cgs = []
for base in bases:
    if (base not in permitted):
        raise Exception("Invalid base: " + base)
    if (base == 'G' or base == 'C'):
        cgs.append(base)
cgPercentage = (float(len(cgs))/len(bases))*100
print cgPercentage
