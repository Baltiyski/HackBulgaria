n = input("Enter number : ");
n = int(n);

startNum = n;
revers = 0;

while(n!=0):
    digit = n % 10;
    revers = revers * 10 + digit;

    n = n // 10;


if(startNum == revers):
    print(str(startNum) + " is palindorm");
else:
    print(str(startNum) + " is not a palindorm");
