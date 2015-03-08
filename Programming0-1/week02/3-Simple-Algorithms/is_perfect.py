n = input("Enter number : ");
n = int(n);

index = 1;
sumDiv = 0;

while(index < n):
    if(n % index == 0):
        sumDiv = sumDiv + index;
    index += 1;


if(sumDiv == n):
    print("Number " + str(n) + " is Perfect!");
else:
    print("Number " + str(n) + " is not Perfect!");
