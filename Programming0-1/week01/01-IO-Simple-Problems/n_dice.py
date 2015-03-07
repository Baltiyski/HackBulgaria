from random import randint

diceSize = input("Enter Size: ");
diceSize = int(diceSize);

result = randint(1, diceSize);

print("The dice rolled: ")
print(result)

