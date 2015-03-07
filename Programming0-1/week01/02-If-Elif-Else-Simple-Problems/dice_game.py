from random import randint

diceSide = input("Enter dice side: ");
diceSide = int(diceSide);

firstPlayer = input("Enter first player: ");
secondPlayer = input("Enter second player: ");

firstPlayerRoll = randint(1, diceSide);
print(firstPlayer + " rolls " + str(firstPlayerRoll));

secondPlayerRoll = randint(1, diceSide);
print(secondPlayer + " rolls " + str(secondPlayerRoll));

if(firstPlayerRoll > secondPlayerRoll):
    print(firstPlayer + " wins!");
elif(firstPlayerRoll < secondPlayerRoll):
    print(secondPlayer + " wins!");
else:
    print("Equal");
