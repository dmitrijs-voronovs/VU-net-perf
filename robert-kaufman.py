K = 4
C = 5

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


def printItem(str):
    print(f"\item ${str}$")


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
