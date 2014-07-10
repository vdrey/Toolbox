# Randomly generate a list of check values to empty a balance.
import random

print('Enter dollar ammount of check values needed.')
amt = input()

checkVals = []

while sum(checkVals) < amt:

    nextVal = random.uniform(0, amt)

    if nextVal + sum(checkVals) > amt:

    else:
        checkVals.append(nextVal)
