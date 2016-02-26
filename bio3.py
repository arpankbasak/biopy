from matplotlib import pyplot

from bio2 import calculate_windows

gesScale = {'F': -3.7, 'M': -3.4, 'I': -3.1,' L': -2.8, 'V': -2.6,
            'C': -2.0, 'W': -1.9, 'A': -1.6,' T': -1.2, 'G': -1.0,
            'S': -0.6, 'P': 0.2, 'Y': 0.7, 'H': 3.0, 'Q': 4.1,
            'N': 4.8, 'E': 8.2, 'K': 8.8, 'D': 9.2,' R': 12.3}

def hydro(prot):
    return sum(map(lambda x: gesScale[x], list(prot.upper())))

print hydro("fcsn")

def hydroWindows(dna, winSize):
    windows = calculate_windows(dna, winSize=winSize)
    return map(lambda x: hydro(x), windows)

prot = 'FMWPEPEPWPFAKYDH'
hydroResults = hydroWindows(prot, 4)
# print gcResults
from matplotlib import pyplot

pyplot.plot( hydroResults )
pyplot.axis([0, 15, -25, 25])
pyplot.ylabel('%Hydrophobicity')
pyplot.title('Hydrophobicity plot')
# pyplot.text(12, .7, "this is some text!")
pyplot.show()