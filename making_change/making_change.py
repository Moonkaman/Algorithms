#!/usr/bin/python

import sys


def making_change(amount, denominations, cache=None):
    if cache == None:
        cache = [0 for i in range(amount+1)]

    cache[0] = 1

    for i in denominations:
        for higher_amount in range(i, amount+1):
            diff = higher_amount - i
            cache[higher_amount] += cache[diff]

    return cache[amount]


'''
0: 1
1: 1
2: 1
3: 1
4: 1
5: 2
6: 2
7: 2
8: 2
9: 2
10: 4
'''


# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
denominations = [1, 5, 10, 25, 50]
print(making_change(12, denominations))
#   print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
# else:
#   print("Usage: making_change.py [amount]")
