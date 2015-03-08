N = input("Enter N: ");
M = input("Enter M: ");

N = int(N);
M = int(M);

lowerBound = 0;
upperBound = 0;

if N < M:
    lowerBound = N;
    upperBound = M;
else:
    lowerBound = M;
    upperBound = N;



start = lowerBound;

while start <= upperBound:

    n = start;
    total_sum  = 0;
    
    while n != 0:
        digit = n % 10;
        total_sum = total_sum + digit;
        n = n // 10;
        
    print("total_sum of digits of " + str(start) + " = " + str(total_sum));
    start += 1;

