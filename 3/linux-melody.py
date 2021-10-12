#!/usr/bin/env python

#
# Solution Template for Melody
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of notes.
# N = None

# K is the number of types of notes (labelled from 1 to K).
# K = None

# S contains the sequence of notes forming the song.
# S = [None for x in range(100005)]

# answer = None

# Open the input and output files.
S = []
with open("melodyin.txt", "r") as input_file:
    N, K = map(int, input_file.readline().strip().split())
    for i in range(0, N):
        S.append(int(input_file.readline().strip()))

# Read the value of N and K.

# Read each note in the song.


# TODO: This is where you should compute your solution. Store the smallest
# possible number of notes Melody can change so that her song is nice into the
# variable answer.

notes = list(set(S))

def most(l):
    most = 0
    most_note = 0
    for i in notes:
        count = l.count(i)
        if count > most:
            most = count
            most_note = i
        if count > len(l)//2:
            break
    return most_note

nice = [most(S[::3]), most(S[1::3]), most(S[2::3])]

answer = 0
for counter in range(N):
    if S[counter] != nice[counter%3]:
        answer += 1

# Write the answer to the output file.
with open("melodyout.txt", "w") as output_file:
    output_file.write("%d\n" % (answer))
