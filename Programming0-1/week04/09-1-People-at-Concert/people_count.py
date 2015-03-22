from random  import randint, shuffle


def get_people_activity(activity):

    list = [];

    for name in activity:
        if name not in list:
            list += [name];

    return len(list);

#Test#########
def generate_test(count):
    names = ["Ivo", "Maria", "Anetta", "Philip", "Rado", "Gergana"]

    result = []

    for name in names:
        result = result + [name] * randint(1, count)
    
    shuffle(result)

    return result

names = generate_test(10)
print(get_people_activity(names));
