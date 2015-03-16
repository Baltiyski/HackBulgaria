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
    found = False;

    for member in xs:
        if(x == member):
            found = True;
            break;
    return found;

def grades_that_pass(students, grades, limit):
    result = [];
    index = 0;

    for grade in grades:
        student = students[index];

        if(grade >= limit):
            result = result + [student];
        index += 1;
    return = result;
