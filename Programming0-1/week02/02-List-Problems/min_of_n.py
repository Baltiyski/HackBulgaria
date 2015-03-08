n = input("Enter lengt : ");
n = int(n);

array = [];
minNum = 0;
index = 0;

while(index < n):
    number = input("Input number for index " + str(index) + " = ");
    number = int(number);

    array = array + [number];
    
    index += 1;

minNum = array[0];
for number in array:
    if(number < minNum):
        minNum = number;

        
print(minNum);
