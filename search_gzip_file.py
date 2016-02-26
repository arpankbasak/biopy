import gzip
import sys
import csv

if len( sys.argv ) != 2:
    print "Usage: %s ACCESSIONFILE " % sys.argv[0]
    sys.exit(1)

genomes = []
accessions = []
accession_file_name = sys.argv[1]
genome_db = {}

with gzip.GzipFile( './data/1000genomes_samples.csv.gz' ) as fobj:
    reader = csv.reader( fobj )
    genomes = list(reader)
    genome_names = [x[1] for x in genomes]
    genome_db = dict(zip(genome_names, genomes))

with open('./data/' + accession_file_name) as accessions:
    reader = csv.reader( accessions )
    accessions = list(reader)

def test(accession, genomes):
    return genome_db.has_key(accession)
    # found = False
    # for record in genomes:
    #     if record[1] == accession:
    #         return True
    # return False

with open('./data/' + accession_file_name + "-results", "w") as resultsFile:
    writer = csv.writer(resultsFile, delimiter=" ")
    for accession in accessions:
        writer.writerow([accession[0], test(accession[0], genomes)])

