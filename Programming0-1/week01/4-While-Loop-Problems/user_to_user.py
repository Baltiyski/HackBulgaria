a = input("Enter a: ");
a = int(a);

b = input("Enter b: ");
b = int(b);

if(a == b):
    print(a);
    print(b);
elif(a < b):
    while(a <= b):
        print(a);
        a += 1;
else:
    while(b <= a):
        print(b);
        b += 1;
