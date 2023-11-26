import math
import numpy as np
from constants import N, l, m, b, states


def productForm(state):
    res = 1
    for i in range(4):
        res *= ((l[i] * m[i]) ** state[i]) / math.factorial(state[i])
    return res


G = 0
for state in states:
    G += productForm(state)

# G = 1

total = 0
probabilities = {}
for state in states:
    res = productForm(state) / G
    total += res
    print(f"pi{state} = {res}")
    probabilities[state] = res

print(f"total = {total}")

# Q9


def blockingProb(n):
    res = 0
    remaining = N - b[n]
    for state in states:
        if (np.dot(list(state), b) <= remaining):
            res += probabilities[state]
    return 1 - res


for i in range(4):
    print(f"blockingProb({i}) = {blockingProb(i)}")

blockProbRes = '''
blockingProb(0) = 0.20438212315335313
blockingProb(1) = 0.4549233947972031
blockingProb(2) = 0.702079807811445
blockingProb(3) = 0.8858049881946004
'''
