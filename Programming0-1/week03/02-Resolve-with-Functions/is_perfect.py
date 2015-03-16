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

def sumDivisor(n):
    return sumInts(divisor(n));

def isPerfect(n):
    return sumDivisor(n) == n;

n = input("Enter n: ")
n = int(n)

print("All number divisor's - " + str(divisor(n)));
print("Sum of all divisor's - " + str(sumDivisor(n)));

if(isPerfect(n)):
    print(str(n) + " is Perfect!");
else:
    print(str(n) + " is not Perfect!");
