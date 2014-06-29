# this is to play around with for loops

print('Enter your target value. (Must be greater than 24)')
TARGET = input()
TARGET = int(TARGET)

termR1 = 5
possList = [2,3]

while termR1 < TARGET:

    possList.append(termR1)
    termR1 = termR1 + 1
    print(possList[len(possList)-1])
    
print(possList)
print()

for divisor in possList:

    
