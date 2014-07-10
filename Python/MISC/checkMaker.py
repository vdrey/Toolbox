# Randomly generate a list of check values to empty a balance.
import random

print('Enter dollar ammount of check values needed.')
amt = input()
print()
print()

checkVals = []

while sum(checkVals) < amt:

    nextVal = random.uniform(0, amt)
    nextVal = round(nextVal, 2)

    if nextVal + sum(checkVals) > amt:

    else:
        checkVals.append(nextVal)

print(check
