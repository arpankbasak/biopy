bases = "AGTCCTAGATGAAAG"
base_list = list(bases)
# for base in base_list:
#     print(base)

# for base_idx in range(2, len(base_list)-1, 3):
    # print base_list[base_idx]

# print [base_list[base_idx] for base_idx in range(2, len(base_list)-1, 3)]

city_pops = {
    'London': 8200000,
    'Cambridge': 130000,
    'Edinburgh': 420000,
    'Glasgow': 1200000
}


cgs = [base for base in bases if (base == 'G' or base == 'C')]
cgPercentage = (float(len(cgs))/len(bases))*100
print cgPercentage
