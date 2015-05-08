def sublist(list1, list2):
    index = 0;

    if(list1 == [] and list2 == []):
        return True;

    if(len(list1)> len(list2)):
        return False;

    if(len(list1) == len(list2)):
        for number in range(0,len(list1)):
            if(list1[number] != list2[number]):
                return False;
            else:
                return True;

    while(index < len(list2)):
        if(list1[0] == list2[index]):
            a = index;
            b = index;

            for number in range(0, len(list1)):
                if(list1[number] == list2[a]):
                   a+=1;

            if(a - b == len(list1)):
                   return True;

        index += 1;

    return False;

y = sublist(["Python"], ["Python", "Django"]);
print(y);

z = sublist([1, 2], [1, 0, 1, 2, 2]);
print(z);

t = sublist([], []);
print(t);

b = sublist(["Django", "Python"], ["Python", "Django"]);
print(b);

i = sublist(["Django", "Python", "Bango"], ["Python", "Django"]);
print(i);
