n = input("Enter lengt : ");
n = int(n);

array = [];
maxNum = 0;
index = 0;

while(index < n):
    number = input("Input number for index " + str(index) + " = ");
    number = int(number);

    array = array + [number];
    
    index += 1;

maxNum = array[0];
for number in array:
    if(number > maxNum):
        maxNum = number;

        
print(maxNum);
