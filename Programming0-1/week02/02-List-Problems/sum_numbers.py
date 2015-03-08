n = input("Enter lenght: ");
n = int(n);

count = 1;
numbers = [];
sumOfAllNumInArray = 0;

while count <= n:
    number = input("Enter number for index " + str(count) + " = ");
    number = int(number);
    
    sumOfAllNumInArray = sumOfAllNumInArray + number;
    
    numbers = numbers + [number];

    count += 1

print("The sum is : " + str(sumOfAllNumInArray));
