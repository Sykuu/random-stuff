import random

length = 100
randNumbers = []
notSorted = True

# Creates a list full of random numbers
for i in range(length):
    randNumbers.append(random.randint(0, 100))

while notSorted:
    # compares every number to its neighbour. if the left one is greater than the right one, they get swapt
    for index, number in enumerate(randNumbers, start=1):
        if index < length and number > randNumbers[index]:
            randNumbers[index - 1] = randNumbers[index]
            randNumbers[index] = number

    notSorted = False

    # Checks if the numbers are sorted. Using break because it makes the checking faster
    for index, number in enumerate(randNumbers, start=1):
        if index < length and number > randNumbers[index]:
            notSorted = True
            break

print(randNumbers)