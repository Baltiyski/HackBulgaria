def is_prime(n):
    index  = 2;
    toPrime = True;

    if(n == 2):
        toPrime = False;

    while(index < n):
        if(n % index == 0):
            toPrime = False;
            break;
        index = index + 1;
    return toPrime;
    
def prime_pair(numbers):
    result = False;

    for x in numbers:
        for y in numbers:
            if(is_prime(x + y)):
                return True;
            
    return False;

numbers = prime_pair([2,2,4,8,9]);
print(numbers)
            
