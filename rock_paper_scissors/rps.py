#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    elements = ['rock', 'paper', 'scissors']
    possible_plays = []

    if n == 0:
        return [[]]
    elif n == 1:
        return elements
    else:
        rps = rock_paper_scissors(n-1)
        for i in range(len(elements)):
            for j in range(3**(n-1)):
                possible_plays += [elements[i] + ' ' + rps[j]]

    return possible_plays


print(rock_paper_scissors(3))


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
