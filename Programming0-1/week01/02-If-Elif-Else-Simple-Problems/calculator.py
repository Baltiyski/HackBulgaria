a = input("Enter a: ");
a = int(a);

b = input("Enter b: ");
b = int(b);

oper = input("Enter operation : ");
result = 0;

if(oper == "+"):
    result = a + b;
    print("Result is: ")
    print(result)
elif(oper == "-"):
    result = a - b;
    print("Result is: ")
    print(result)
elif(oper == "*"):
    result = a * b;
    print("Result is: ")
    print(result)
elif(oper == "/"):
    result = a / b;
    print("Result is: ")
    print(result)
else:
    print("Wrong operation");
