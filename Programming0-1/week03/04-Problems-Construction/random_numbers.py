from random import randint
def generate_random_list(n, start, end):
    result = [];
    index = 0;

    while(index < n):
        nextNumber = randint(start, end);
        result = result + [nextNumber];

        index += 1;
    return result;

n = input("Lenght for array : ");
n = int(n);

start = input("Frome which number to start : ");
start = int(start);

end = input("For which number to end : ");
end = int(end);

print(generate_random_list(n, start, end));
