def head(items):
    return items[0];

def last(items):
    last_item = len(items) - 1;
    return items[last_item];

def tail(items):
    result [];

    for index in range(1, len(items)):
        item += items[index];
        result += [item];

    return result;
    
def equal_list(listOne, listTwo):
    if(len(listOne) != len(listTwo)):
        return False;

    for index in range(0, len(listOne)):
        if(listOne[index] != listTwo[index]):
            return False;

    return True;

def count_item(item, list1):
    result = 0;

    for index in list1:
        if(index == item):
            result += 1;

    return result;

def take(num, list1):
    result = [];

    for index in range(0, min(num, len(list1))):
        result += [list1[index]];

    return result;

def drop(num, list1):
    result = [];

    for index in range(num, len(list1)):
        result += [list1[index]];

    return result;

def reverse(arr):
    result = [];

    last_index = len(arr) - 1;

    while last_index >= 0:
        result += [arr[last_index]];
        last_index -= 1;

    return result;
