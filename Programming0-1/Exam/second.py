def reverse(arr):
    result = [];

    for itm in arr:
        result = [itm] + result;

    return result;

def second_largest(numbers):
    numbers = reverse(sorted(numbers));
    arr = [];

    for number in numbers:
        if(number not in arr):
            arr += [number];

    if(len(arr) < 2):
        return False;

    return arr[1]

print(second_largest([]));
print(second_largest([2, 1]));
print(second_largest([5, 5]));
print(second_largest([100, 100, 90]));
