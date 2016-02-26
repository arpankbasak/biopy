import sys

filename = sys.argv[1]

try:
    with open("./data/"+filename, 'r') as sequence_file:
        for sequence in sequence_file.readlines():
            print len(sequence.rstrip())
except IOError:
    print "No such file", filename, "in data directory"
