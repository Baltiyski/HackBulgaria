number = input("Enter number: ");
number = int(number);

while(number != 0):
    digit = number % 10;
    print(digit);
    number = number // 10;
