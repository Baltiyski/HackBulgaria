n = input("Enter lengt : ");
n = int(n);

array = [];
index = 0;
sumOfNum = 0;

while(index < n):
    number = input("Input number for index " + str(index) + " = ");
    number = int(number);
    
    sumOfNum = sumOfNum + number;
    
    array = array + [number];

    index += 1;

avg = sumOfNum / n;

print ("Avg is = " +str(avg));
