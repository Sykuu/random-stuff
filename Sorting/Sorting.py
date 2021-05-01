import random

length = 100
randNumbers = []
notSorted = True

# Creates a list full of random numbers
for i in range(length):
    randNumbers.append(random.randint(0, 100))

while notSorted:
    # compares every number to its neighbor. if the left one is greater than the right one, they get swapt until the list is sorted
    notSorted = False
    for index, number in enumerate(randNumbers, start=1):
        if index < length and number > randNumbers[index]:
            randNumbers[index - 1] = randNumbers[index]
            randNumbers[index] = number
            notSorted = True

print(randNumbers)