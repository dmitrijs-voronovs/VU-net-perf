from constants import K, C, l, m, b, states
from utils import printItem

memo = {}


def g(c):
    if (c == 0):
        return 1
    if (c < 0):
        return 0
    if (c in memo):
        return memo[c]

    total = sum([b[j] * l[j] * m[j] * g(c - b[j]) for j in range(K)])
    res = 1 / c * total
    memo[c] = res
    return res


G = sum([g(i) for i in range(C + 1)])
q = {}
for c in range(0, C+1):
    q[c] = g(c) / G

for j in range(K):
    B = sum([q[c] for c in range(C-b[j]+1, C+1)])
    printItem(f"B_{j+1}={B}")
