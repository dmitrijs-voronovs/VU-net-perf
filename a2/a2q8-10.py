import math


def ceildiv(a, b):
    return -(-a // b)


# Define formula for transfer time
def transfer_time(fs, cw_start, rtt):
    S = ceildiv(fs, 1_460)
    R = math.floor(math.log2(ceildiv(S, cw_start)) + 1)
    print(f"S={S} R={R}")

    return \
        rtt + 0.05 + \
        R * rtt + \
        (fs * 8) / 100_000_000


# Calculate transfer times for assignment 8
print("Assignment 8")
for fs in [10_000, 20_000, 50_000]:
    print(f"fs={fs} t_transfer = {transfer_time(fs, 1, 0.05)} seconds")

# Calculate transfer times for assignment 9
print("Assignment 9")
for fs in [10_000, 20_000, 50_000]:
    print(f"fs={fs} t_transfer = {transfer_time(fs, 5, 0.05)} seconds")

# Calculate transfer times for assignment 10
print("Assignment 10")
for fs in [10_000, 20_000, 50_000]:
    print(f"fs={fs} t_transfer = {transfer_time(fs, 1, 0.1)} seconds")
