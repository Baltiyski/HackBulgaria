def square(x):
    return x ** 2;

def factorial(f):
    index = 1;
    fact = 0;

    while(index <= f):
        fact = fact * index;
        index += 1;
    return fact;
    
def countElements(items):
    arrayLenght = 0;

    for it in items:
        arrayLenght += 1;

    return arrayLenght;

def member(x, xs):
    
