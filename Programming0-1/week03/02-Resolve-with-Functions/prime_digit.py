def isPrime(n):
    if(n <= 1):
        return False;

    isPrime = True;

    index = 2;

    while(index < n):
        if(n % index == 0):
            isPrime = False;
            break;

        index += 1;

    return isPrime;

def toDigits(n):
    result = [];

    while(n != 0):
        digit = n % 10;
        result = result + [digit];

        n = n // 10;

    return result;

n = input("Enter n : ");
n = int(n);

digits = toDigits(n);

primeDigits = False;

for digit in digits:
    if(isPrime(digit)):
       primeDigits = True;
       break;

if primeDigits:
       print("There are prime digits!");
else:
       print("There are no prime digits!");
