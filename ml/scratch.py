import math
import numpy as np
scores = [2.5, 0.3, 2.8, 0.5]
indicators = [1,0,1,1]

def prob(score):
    return 1/(1+ math.exp(-score))


def probs(scores, indicators):
    result = []
    for i in range(len(scores)):
        if (indicators[i] == 1):
            result.append(prob(scores[i]))
        else:
            result.append(1-prob(scores[i]))
    return result

score_probs = probs(scores,indicators)
print score_probs
liklihood = np.prod(np.array(score_probs))
print liklihood


derivative = sum(np.array(np.array(indicators) - np.array(score_probs)) * np.array(scores))

print derivative

