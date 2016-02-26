import sys
print sys.argv
try:
    ops = map(lambda x: int(x), sys.argv[1:])
    print sum(ops)
except ValueError:
    print "All arguments must be numerical"

