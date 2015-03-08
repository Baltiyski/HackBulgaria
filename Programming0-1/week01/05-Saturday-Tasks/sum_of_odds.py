n = input("Enter n: ");
n = int(n);

sumOfOdd = 0;
index = 1;

while(index <= n):
    if(index % 2 != 0):
        sumOfOdd += index;
    index += 1;
print("Sum of all evens = " + str(sumOfOdd))

