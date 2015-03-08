n = input("Enter number : ");
n = int(n);

startIndex = 1;
factorial = 1;

while(startIndex <= n):
    factorial = factorial * startIndex;
    startIndex += 1;

print("Factorial of N = " + str(factorial));
