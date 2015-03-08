searchWord = input("Enter word : ");

n = input("Enter lengt : ");
n = int(n);

array = [];
index = 0;
sumOfWords = 0;

while(index < n):
    number = input("Input word for index " + str(index) + " = ");

    array = array + [number];

    index += 1;


for word in array:
    if(searchWord in word):
        sumOfWords += 1;

print(searchWord + " is found " + str(sumOfWords) + " times.");
