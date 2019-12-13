#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

def eating_cookies(n, cache = None):
  # Initialize cache
  if cache is None:
    cache = [0 for i in range(n + 1)]
  # handle case for n = 0
  cache[0] = 1
  # handle case for n < 0
  if n < 0:
    return 0
  # If there is no value in the cache, set a permutation counter
  # for the range of combinable numbers (0, 1, 2, 3), find the sum
  # of the permutations by recursively adding them together
  elif cache[n] == 0:
    permutations = 0
    for amount in range(1, 4):
      permutations += eating_cookies(n - amount, cache)
    cache[n] = permutations
  # If n is in the cache, return that value to be added to the permutation total
  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')