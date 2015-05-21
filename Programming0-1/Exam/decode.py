def stringToList(fString):

    result = [];

    for ch in fString:
        result += [ch];
        
    return result;

def listToString(fList):
    result = "";

    for itm in fList:
        result += itm;

    return result;

def decodeWord(encryptedWord, cipher):
    encryptedWord = stringToList(encryptedWord);
    result = [];

    for itm in encryptedWord:
        for key in cipher:
            if(itm == cipher[key]):
                result += [key];

    return listToString(result);


print(decodeWord("mjriew", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'}));
print(decodeWord("rpf", {'m': 'p', 'o': 'r', 'g': 'f'}));
print(decodeWord("wfhsftzzuys", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'}));
print(decodeWord("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'}));
