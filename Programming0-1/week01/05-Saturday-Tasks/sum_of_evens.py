n = input("Enter n: ");
n = int(n);

sumOfEvens = 0;
index = 1;

while(index <= n):
    if(index % 2 == 0):
        sumOfEvens += index;
    index += 1;
print("Sum of all evens = " + str(sumOfEvens))
