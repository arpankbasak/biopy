import math
import numpy as np

tuples = [(1,-1), (1,1), (-1,-1), (-1, -1), (1,-1)]
equals = [x!=y for (x,y) in tuples]

print float(sum(equals))/len(tuples)


