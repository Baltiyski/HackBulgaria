def divisor(n):
    index = 1;
    result = [];
    

    while(index < n):
        if (n % index == 0):
            result = result + [index];
        index +=1 ;
        
    return result;

def sumInts(numbers):
    result2 = 0;
    index = 1;

    for number in numbers:
        result2 += number;

    return result2

num = input("Enter n: ");
num = int(num);

print(divisor(num));
print(sumInts(divisor(num)));
