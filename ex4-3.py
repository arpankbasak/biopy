import sys
import csv

filename = sys.argv[1]
genes = None
try:
    with open("./data/"+filename, 'r') as gene_file:
        reader = csv.reader( gene_file, delimiter = "\t" )
        genes = list(reader)
except IOError:
    print "No such file", filename, "in data directory"

print genes

with open("./data/"+filename+"-out", 'w') as gene_size_file:
    writer = csv.writer(gene_size_file, delimiter=" ")
    for g in genes:
        writer.writerow([g[0], str(int(g[3]) - int(g[2]))])
