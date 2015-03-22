def count_zero_neighbours(numbers):

    index = 0;
    result = 0;
    
    for number in numbers:
        if(index < len(numbers) - 1):
            if(numbers[index] + numbers[index + 1] == 0):
                result += 1;
        index += 1;

    return result;

result2 = count_zero_neighbours([1, 2, -2, 0, 0, 5, -5]);
print(result2)
