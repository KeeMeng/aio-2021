#!/usr/bin/env python

#
# Solution Template for Space Mission
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.

# N is the number of available days.
N = None

# F is the amount of fuel available.
F = None

# C contains the fuel needed to open a portal on each day.
C = [None for x in range(100005)]

with open("spacein.txt", "r") as input_file:
    # Read the value of N and F.
    input_line = input_file.readline().strip()
    N, F = map(int, input_line.split())

    # Read the cost to open a portal on each day.
    for i in range(0, N):
        C[i] = int(input_file.readline().strip())

# TODO: This is where you should compute your solution. Store the maximum
# number of samples you could collect into the variable answer.
if N == 2:
    if C[0] + C[1] > F:
        answer = -1
    else:
        answer = 2
else:
    answer = 0
    for start in range(N):
        for end in range(start+answer, N):
            if C[start] + C[end] <= F:
                answer = end-start
    if answer > 0:
        answer += 1
    else:
        answer = -1


# Write the answer to the output file.
with open("spaceout.txt", "w") as output_file:
    output_file.write("%d\n" % (answer))
