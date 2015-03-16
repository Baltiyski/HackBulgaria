def toDigit(n):
    result = [];

    while(n != 0):
        digit = n % 10;
        result = [digit] + result;

        n = n // 10;
    return result;

def toNumber(digits):
    result = 0;

    for digit in digits:
        result = result * 10 + digit;

    return result;

def maxNumber(n):
    digits = toDigit(n);

    digits = sorted(digits, reverse = True );

    return toNumber(digits);

def minNumber(n):
    digits = toDigit(n);
    digits = sorted(digits);

    return toNumber(digits);
        
n = input("Enter number : ");
n = int(n);

print("Max Number - " + str(maxNumber(n)));
print("Min number - " +  str(minNumber(n)));
