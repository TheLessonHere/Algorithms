#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Initialize cache
  cache = [0 for i in range(amount + 1)]
  # Handle case for amount = 0 cents
  cache[0] = 1
  # Define nested recursive function to iterate over each amount and denomination
  def recur_change(amount, denominations, cache):
    # If we hit negatives, return 0 (i.e. if an amount is less than the coin we are checking)
    if amount < 0:
      return 0
    # Otherwise if the amount has not already been checked and cached...
    elif cache[amount] == 0:
      # Iterate over each possible coin amount in denominations
      for coin in denominations:
        # For each coin, iterate over the higher amounts between the coin value and the starting amount
        for higher_amount in range(coin, amount + 1):
          # For each amount (higher_amount), set the value of the cache for the higher amount equal to the recursive sum
          # decrementing the amount by the coin each time until it hits our base case
          cache[higher_amount] += recur_change(higher_amount - coin, denominations, cache)
    # If the amount HAS already been checked and cached, return the number for the given amount to end the recursion
    return cache[amount]
  # Call our recursive function to begin the loop
  return recur_change(amount, denominations, cache)


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")