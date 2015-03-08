n = input("Enter number : ");
n = int(n);

index = 1;

while(index < n):
    if(n % index == 0):
        print(index)
    index += 1;
