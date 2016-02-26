def calculate_windows(seq, winSize):
    """This function takes a given sequence (seq) and a sliding window size (WinSize)
    and returns all sub-sequences acording to the size of the sliding window.
    Notice that the sub-sequences are overlapping and their size is fixed according to winSize.
    """
    if winSize <= 0:
        raise Exception("Window size must be a positive integer")
    if winSize > len(seq):
        raise Exception("Window size is larger than sequence length")
    result = []
    nrWindows = len(seq)-winSize+1
    for i in range(nrWindows):
        subSeq = seq[i:i+winSize]
        result.append(subSeq)
    return result


def cgPercentage(dna):
    cgs = [base for base in dna if (base.upper() == 'G' or base.upper() == 'C')]
    return (float(len(cgs))/len(dna))*100


dna = 'AGATACTAGCATGACAGATTGTGGGCCGCATAGAAATATAGACA'

def cgWindows(dna, winSize):
    windows = calculate_windows(dna, winSize=winSize)
    return map(lambda x: cgPercentage(x), windows)

# gcResults = cgWindows(dna, 20)
# # print gcResults
# from matplotlib import pyplot
#
# pyplot.plot( gcResults )
# pyplot.axis([0, 50, 20, 60])
# pyplot.ylabel('%GC')
# pyplot.title('GC plot')
# pyplot.text(12, .7, "this is some text!")
# pyplot.show()