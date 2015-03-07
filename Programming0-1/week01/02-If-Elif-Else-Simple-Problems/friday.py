import time

today = time.strftime("%A");
print(today);


if((today == "Friday") or (today == "friday")):
    print("It is friday!");
else:
    print("It is not friday ;( Today is " + today);
