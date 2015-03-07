print("Input some text : ");
someWords = input();

if(("hello" in someWords) or ("Hello" in someWords)):
    print("Hello there, good stranger!");
elif("how are you?" in someWords):
    print("I am fine, thanks. How are you?");
elif("feelings" in someWords):
    print("I am a machine. I have no feelings");
elif("age" in someWords):
    print("I have no age. Only current timestamp");
