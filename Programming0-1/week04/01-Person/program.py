firstName = input("Enter first name: ");
middleName = input("Enter second name: ");
lastName = input("Enter last name: ");
birthYear = input("Enter year of birth: ");
birthYear = int(birthYear);

person = {};

person["firstName"] = firstName;
person["middleName"] = middleName;
person["lastName"] = lastName;
person["birthYear"] = birthYear;
person["age"] = 2015 - birthYear;

for key in person:
    value = person[key];

    print(key, value);
