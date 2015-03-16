def divisor(n):
    index = 1;
    result = [];
    

    while(index <= (n - 1)):
        if (n % index == 0):
            result = result + [index];
        index +=1 ;
        
    return result;

n = input("Enter number : ");
n = int(n);

print(divisor(n));
