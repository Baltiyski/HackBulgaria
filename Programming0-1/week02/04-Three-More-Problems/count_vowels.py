vowels = "aeiouyAEIOUY";
count = 0;

string = input("Input some word's: ");

for ch in string:
    if ch in vowels:
        count += 1;

print(count);
