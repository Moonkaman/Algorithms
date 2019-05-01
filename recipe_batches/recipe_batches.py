#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = []
    for ingred in recipe:
        if ingred in ingredients:
            amount = ingredients[ingred] / recipe[ingred]
            if amount < 1:
                return 0
            else:
                batches.append(math.floor(amount))
        else:
            return 0
    return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 5, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
