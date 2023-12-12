import matplotlib.pyplot as plt
import numpy as np


traffic = np.zeros(shape=46)
traffic[0:10] = 5
traffic[15:20] = 8
traffic[25:46] = 2.5


# task 5 and 6
def apply_policing(traffic, leak_rate, burst_tolerance):
    conforming_traffic = np.zeros(len(traffic) + 1)
    nonconforming_traffic = np.zeros(len(traffic) + 1)
    bucket_level = burst_tolerance  # bucket starts full

    for i in range(len(traffic)):
        bucket_level = min(bucket_level + leak_rate, burst_tolerance)
        bucket_level_used = min(bucket_level, traffic[i])
        bucket_level -= bucket_level_used
        conforming_traffic[i + 1] += bucket_level_used
        nonconforming_traffic[i + 1] += traffic[i] - conforming_traffic[i + 1]

    return (conforming_traffic, nonconforming_traffic)


# Plot for task 5
def plot_policed_traffic(policed_traffic, file='a2q5.png'):
    plt.step(range(len(policed_traffic)), policed_traffic, color='blue')
    plt.xlabel('Time')
    plt.ylabel('Bitrate (Mbit/s)')
    plt.title('Bitrate of Traffic after Policing over Time')
    plt.grid(True)
    plt.savefig(file)
    plt.show()


# Plot for task 6
def plot_conforming_v_nonconforming_traffic(conforming_traffic, nonconforming_traffic, file='a2q6.png'):
    plt.step(range(len(conforming_traffic)), conforming_traffic, color='blue', label='Conforming traffic')
    plt.step(range(len(nonconforming_traffic)), nonconforming_traffic, '--', color='red', label='Nonconforming traffic')
    plt.xlabel('Time')
    plt.ylabel('Bitrate (Mbit/s)')
    plt.title('Conforming and Nonconforming Traffic over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig(file)
    plt.show()


leak_rate = 4
burst_tolerance = 1 * 8  # Burst tolerance in Mbit (1 Mbyte = 8 Mbit)

conforming_traffic, nonconforming_traffic = apply_policing(traffic, leak_rate, burst_tolerance)
plot_policed_traffic(conforming_traffic)
plot_conforming_v_nonconforming_traffic(conforming_traffic, nonconforming_traffic)

# Task 7
leak_rate = 2
conforming_traffic, nonconforming_traffic = apply_policing(traffic, leak_rate, burst_tolerance)
plot_policed_traffic(conforming_traffic, file='a2q7a.png')
plot_conforming_v_nonconforming_traffic(conforming_traffic, nonconforming_traffic, file='a2q7b.png')