#!/usr/bin/python

import argparse


def find_max_profit(prices):
    biggest = 0
    biggest_ind = 0
    smallest = 99999999999999999999999999999999999999
    for i in range(len(prices)):
        if i != 0 and prices[i] > biggest:
            biggest = prices[i]
            biggest_ind = i
    for price in prices[:biggest_ind]:
        if price < smallest:
            smallest = price
    return biggest - smallest


print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95,
                       43, 11, 47, 67, 89, 42, 49, 79]))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
