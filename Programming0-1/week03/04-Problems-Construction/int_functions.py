def reverse_int(n):
    revers = 0;
    
    while(n != 0):
        digit = n % 10;
        revers = revers * 10 + digit;

        n = n // 10;
    return revers;

def sum_digits(n):
    result = 0;

    while(n != 0):
        digit = n % 10;
        result = result + digit;
        n = n // 10;
    return result;

def product_digits(n):
    result = 1;

    while(n != 0):
        digit = n % 10;
        result *= digit;
        n = n // 10;
    return result;

n = input("Enter number : ");
n = int(n);

print(reverse_int(n));
print(sum_digits(n));
print(product_digits(n));
