import math
import numpy as np

N = 5

# Define the coefficients
l_1 = 24
l_2 = 0.504
l_3 = 0.144
l_4 = 0.072
m_1 = 0.167
m_2 = 0.05
m_3 = 0.05
m_4 = 0.05
# -----------------------
# l_1 = 24
# l_2 = 0.504
# l_3 = 0.144
# l_4 = 0.072
# m_1 = 3.6
# m_2 = 0.72
# m_3 = 0.72
# m_4 = 0.72
l = [l_1, l_2, l_3, l_4]
m = [m_1, m_2, m_3, m_4]
b = [1, 2, 3, 4]

states = [
    (2, 0, 1, 0),
    (1, 0, 1, 0),
    (0, 0, 1, 0),
    (0, 1, 1, 0),
    (0, 0, 0, 1),
    (0, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 2, 0, 0),
    (1, 0, 0, 1),
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (1, 2, 0, 0),
    (2, 0, 0, 0),
    (2, 1, 0, 0),
    (3, 0, 0, 0),
    (3, 1, 0, 0),
    (4, 0, 0, 0),
    (5, 0, 0, 0),
]


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
