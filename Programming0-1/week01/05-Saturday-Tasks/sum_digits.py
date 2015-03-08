number = input("Enter number: ");
number = int(number);

sumOf = 0;

while(number != 0):
    digit = number % 10;
    sumOf = sumOf + digit
    number = number // 10;

print("The sum of all number's is equal to - " + str(sumOf));
