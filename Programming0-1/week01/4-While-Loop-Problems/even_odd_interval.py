a = input("Enter a: ");
a = int(a);

b = input("Enter b: ");
b = int(b);

if(a == b):
    print(a);
    print(b);
elif(a < b):
    while(a <= b):
        if(a % 2 == 0):
            print(str(a) + " - even");
        else:
            print(str(a) + " - odd");
        a += 1;
else:
    while(b <= a):
        if(b % 2 == 0):
            print(str(b) + " - even");
        else:
            print(str(b) + " - odd");
        b += 1;
