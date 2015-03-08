n = input("Enter a number: ");
n = int(n);

reversedNumber = 0;

while n != 0:
    digit = n % 10;

    reversedNumber = reversedNumber * 10 + digit;

    n = n // 10;

print("The reversed number is: " + str(reversedNumber));
