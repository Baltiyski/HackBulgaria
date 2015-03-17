def count_vowels_consonants(word):
    dict = {
        "vowels" : 0,
        "consonants" : 0
        }

    vowels = "aeiouyAEIOUY";
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ";

    for char in word:
        if(char in vowels):
            dict['vowels'] += 1;
        else:
            dict['consonants'] += 1;

    return dict;

word = input("Some text : ");

print(count_vowels_consonants(word));
