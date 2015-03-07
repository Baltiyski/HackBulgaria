from random import randint

diceSize = input("Enter sides: ");
diceSize = int(diceSize);
sumOfAllDice = 0;

firstRow = randint(1, diceSize);
print("First Row: ");
print(firstRow);
secondRow = randint(1, diceSize);
print("First Second: ");
print(secondRow);
thirdRow = randint(1, diceSize);
print("First Third: ");
print(thirdRow);

sumOfAllDice = firstRow + secondRow + thirdRow;
print("Sum is: ")
print(sumOfAllDice)
