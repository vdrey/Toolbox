# Randomly generate a list of check values to empty a balance.
import random

print('Enter dollar ammount of check values needed.')
amt = input()
print()
print()

checkVals = []

while sum(checkVals) < float(amt):

    nextVal = random.uniform(0, float(amt))
    nextVal = round(nextVal, 2)

    if nextVal + sum(checkVals) > float(amt):
        print('Nope')

    else:
        checkVals.append(nextVal)

print(checkVals)
print()
print()
print(len(checkVals))
