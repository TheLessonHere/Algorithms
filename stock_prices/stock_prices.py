#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # Set current minimum price to the first item in the list to start
    cur_min_price = prices[0]
  # Set maximum profit so far to a ridiculously low number to start
    max_profit = -10**10001
    # Loop over the array checking each price against the current minimum price
    for i in range(len(prices)):
      # If the current indexed price is higher than the minimum, check its profit margin against the current minimum price
      if prices[i] > cur_min_price:
        profit = prices[i] - cur_min_price

        # Then if the profit margin returned is higher than the current max profit, it becomes the new max profit
        if profit > max_profit:
          max_profit = profit

      # In the case that the prices on the list grow smaller and smaller and there is never a positive max profit
      elif i == len(prices) - 1 and prices[i] < cur_min_price:
        # Sets the max profit to the least amount of money we could have possible lost,
        # which is the min price - the previous min price
        if prices[i] - cur_min_price > max_profit:
          max_profit = prices[i] - cur_min_price

      # If the current indexed price is lower than the current minimum it becomes the new minimum
      elif prices[i] < cur_min_price:
        cur_min_price = prices[i]

    return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))