#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[51]:


# 1
traffic = np.zeros(shape=46)
traffic[0:11] = 5
traffic[15:21] = 8
traffic[25:46] = 2.5


# In[52]:


plt.step(range(len(traffic)), traffic, where='post', color='blue')


# In[1]:


# task 7
# Given parameters
RTT = 50  # Round-Trip Time in milliseconds
receive_CW_size = 256 * 1024  # Receive CW size in Bytes
bandwidth = 100 * 10**6  # Bandwidth in bits per second
MSS = 1460  # Maximum Segment Size in Bytes
processing_time = 50  # Request processing time in milliseconds

# Convert RTT to seconds
RTT_sec = RTT / 1000  # Convert milliseconds to seconds

# Calculate initial CW size in bytes
initial_CW_size = MSS

# Calculate effective bandwidth in bytes per second
effective_bandwidth = bandwidth / 8  # Convert bits to Bytes
initial_window = initial_CW_size

# Function to calculate transfer time for a given file size
def calculate_transfer_time(file_size):
    segments = (file_size + processing_time) / MSS  # Calculate the number of segments needed
    transfer_time = RTT_sec * ((segments - 1) / 2 + 1)  # Calculate transfer time in seconds
    return transfer_time

# Calculate transfer times for different file sizes
file_sizes = [10 * 1024, 20 * 1024, 50 * 1024]  # File sizes in Bytes

for file_size in file_sizes:
    transfer_time = calculate_transfer_time(file_size)
    print(f"Transfer time for {file_size / 1024} KB file: {transfer_time:.5f} seconds")

