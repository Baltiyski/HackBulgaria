n = input("Enter n: ");
n = int(n);

m = input("Enter m: ");
m = int(m);

nLasstNum = n % 10;
mLasstNum = m % 10;

if(nLasstNum > mLasstNum):
    print(n);
elif(mLasstNum > nLasstNum):
    print(m);
else:
    print("Equal");
