n = input("Enter number : ");
n = int(n);

start = 2;
isPrime = True;

while(start < n):
    if(n % start == 0):
        isPrime = False;
        break;
    else:
        isPrime = True;
    start += 1;


if(isPrime == False):
    print("The number is not Prime!");
else:
    print("The number is Prime!");
