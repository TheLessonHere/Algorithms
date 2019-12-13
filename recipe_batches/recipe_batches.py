#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Set a batches counter to 0 by default.
  total_batches = 0
  # Declare a running list which keeps track of the amount of batches each ingredient allows.
  batch_list = []
  # Iterate over the amount of keys in the recipe.
  for key in recipe.keys():
    # For each key, check if it exists in our ingredient list, and if not, return 0 by default.
    if key not in ingredients:
      return 0
    # Otherwise, if it exists, set a variable equal to the number of batches
    # we could make with that particular ingredient.
    else:
      batches = ingredients[key]//recipe[key]
      # Check if any of the batch amounts is less than 0 and return 0 by default if so.
      if batches < 1:
        return 0
      # Otherwise append the amount of batches into our batch list and set total batches
      # equal to the smallest number on the batch list which is the greatest common denominator
      # and thus the max number of batches allowed.
      else:
        batch_list.append(batches)
      total_batches = min(batch_list)

  return total_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))