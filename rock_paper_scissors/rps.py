#!/usr/bin/python

import sys
# Define list with all possible plays
rps = ["rock", "paper", "scissors"]

def rock_paper_scissors(n):
  # Define variable to hold our list of plays
  plays = [[]]
  # In case n < 1 return an empty list
  if n < 1:
    return plays
  # Define a recursive function to protect the logic of the larger function
  def recur_rps(n):
    # Call on plays as a nonlocal variable so that our function has access to mutate it
    nonlocal plays
    # If n is 1 essentially, return each individual play from rps
    if n < 2:
      return [[play] for play in rps]
    # Otherwise, recur and decrement n until it hits our base cases
    else:
      plays = recur_rps(n - 1)
      # Declare a higher scope variable to keep track of the result of adding new possible plays
      result = []
      # Loop over current possible plays
      for play in plays:
        # Declare a higher scope variable to keep track of new plays to be added
        new_plays = []
        # Loop over possible plays (rock, paper, scissors)
        for item in rps:
          # For each current possible play this adds, another combination with each of the
          # items possible to throw (rock, paper, scissors)
          new_plays.append(play + [item])
        # Set result to the new result
        result = result + new_plays
      return result
  # Call the first instance of the recursive function
  return recur_rps(n)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')