#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Social Distancing
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of meals.
# N = None

# K is the minimum distance between hippos.
# K = None

# D contains the locations of the meals.
D = set()

answer = None

# Open the input and output files.
input_file = open("distin.txt", "r")
output_file = open("distout.txt", "w")

# Read the value of N and K.
input_line = input_file.readline().strip()
N, K = map(int, input_line.split())

# Read the locations of the meals.
for i in range(0, N):
    D.add(int(input_file.readline().strip()))

# TODO: This is where you should compute your solution. Store the maximum
# number of hippos that can be invited into the variable answer.

answer = 0

if K == 1:
    answer = len(D)
elif N == 2:
    if len(D) == 1:
        answer = 1
    elif len(D) == 2:
        if abs(list(D)[0] - list(D)[1]) >= K:
            answer = 2
        else:
            answer = 1


# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
