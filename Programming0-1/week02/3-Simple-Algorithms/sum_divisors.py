n = input("Enter number : ");
n = int(n);

index = 1;
sumDiv = 0;

while(index < n):
    if(n % index == 0):
        print(index);
        sumDiv = sumDiv + index;
    index += 1;
print("Sum of all divider's is equal to - " + str(sumDiv));
