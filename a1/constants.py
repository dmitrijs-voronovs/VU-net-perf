N = 5
K = 4
C = 5

# Define the coefficients
l_1 = 24 / 60
l_2 = 0.504 / 60
l_3 = 0.144 / 60
l_4 = 0.072 / 60
d_1 = 6
d_2 = d_3 = d_4 = 20
m_1 = 1/d_1
m_2 = 1/d_2
m_3 = 1/d_3
m_4 = 1/d_4
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
d = [d_1, d_2, d_3, d_4]
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
