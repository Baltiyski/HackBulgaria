languages = ["Python", "Ruby"];
languages = languages + ["C++", "Java", "C#"];
languages = ["Haskell"] + languages;
languages = languages + ["Goo"];

print(languages[0]);
print(languages[1]);
print(languages[4]);

cSharp = "C#";
index  = 0;
while(index < len(languages)):
    if(languages[index] == str(cSharp)):
        languages[index] = "F#"
    index += 1;

print(languages);

