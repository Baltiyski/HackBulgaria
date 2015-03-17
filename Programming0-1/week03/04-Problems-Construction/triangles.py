def is_triangle(a, b, c):
    return a+b>c and a+c>b and b+c>a;

def area(a, b, c):
    p = (a + b + c) / 2;

    return sqrt(p * (p - a) * (p - b) * (p - c));

def is_pythagorean(a, b, c):
    return a ** 2 + b ** 2 + c ** 2;

def max_area(triangles):
    currentMax = triangles[0];

    a = currentMax[0];
    b = currentMax[1];
    c = currentMax[2];

    currentMaxArea = area(a, b, c);

    for triangle in triangles:
        a = triangle[0];
        b = triangle[1];
        c = triangle[2];

        currentArea = area(a, b, c);

        if currentArea > currentMaxArea:
            currentMax = triangle;
            currentMaxArea = currentArea;

    return currentMax;
