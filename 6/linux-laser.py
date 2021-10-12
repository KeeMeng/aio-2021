#!/usr/bin/env python

#
# Solution Template for Laser Cutter
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the side length of the initial square.
# N = None

# A contains the first sequence of instructions.
# A = None

# B contains the second sequence of instructions.
# B = None


# Open the input and output files.
with open("laserin.txt", "r") as input_file:
	# Read the value of N and the sequences of instructions from the input file.
	N = int(input_file.readline().strip())
	A = input_file.readline().strip()
	B = input_file.readline().strip()

# TODO: This is where you should compute your solution. Store the side length
# of the largest square that fits inside the shape into the variable answer.

a = A.split("D")
b = B.split("D")

# distance = [0 for i in range(N)]
# left = [0 for i in range(N)]
# right = [0 for i in range(N)]
# l = 0
# r = 0
# for i in range(N):
# 	l += a[i].count("R")
# 	r += b[i].count("R")
# 	distance[i] = r - l
# 	left[i] = l
# 	right[i] = r

distance = [0 for i in range(N)]
r = 0
for i in range(N):
	r += len(b[i])
	distance[i] = r

# print(distance)
# print(left)
# print(right)

answer = 0
for i in range(1, max(distance)+1)[::-1]:
	if i <= distance.count(i):
		answer = i
		break

# points = [(0,0)]
# old = ""
# for i in A:




# Write the answer to the output file.
with open("laserout.txt", "w") as output_file:
	output_file.write("%d\n" % (answer))